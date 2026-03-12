from __future__ import annotations

import socket
from typing import Any

TEST_DOMAINS = [
    "example.com",
    "cloudflare.com",
    "google.com",
    "openai.com",
]


def _detect_resolver_ip() -> str:
    """Return resolver-observed public IP via OpenDNS if available."""
    try:
        return socket.gethostbyname("myip.opendns.com")
    except socket.gaierror:
        return "Unavailable"


def run_dns_leak_test() -> dict[str, Any]:
    """Perform a basic DNS consistency check using system resolver."""
    issues: list[str] = []
    resolved_count = 0

    for domain in TEST_DOMAINS:
        try:
            # gethostbyname_ex returns (hostname, aliaslist, ipaddrlist)
            _, _, ips = socket.gethostbyname_ex(domain)
            if not ips:
                issues.append(f"No A record resolved for {domain}")
                continue

            resolved_count += 1

            for ip in ips:
                # Private IPs in public domain lookups can indicate interception.
                if ip.startswith(("10.", "172.16.", "192.168.")):
                    issues.append(f"{domain} resolved to private IP {ip}")
        except socket.gaierror as exc:
            issues.append(f"Failed to resolve {domain}: {exc}")

    resolver_ip = _detect_resolver_ip()

    return {
        "resolver_ip": resolver_ip,
        "resolved_domains": resolved_count,
        "potential_issues": len(issues),
        "issues": issues,
    }


if __name__ == "__main__":
    result = run_dns_leak_test()
    print(f"Configured DNS resolver IP: {result['resolver_ip']}")
    print(f"Resolved test domains: {result['resolved_domains']}")
    print(f"Potential issues detected: {result['potential_issues']}")
    if result["issues"]:
        print("Details:")
        for item in result["issues"]:
            print(f"- {item}")
