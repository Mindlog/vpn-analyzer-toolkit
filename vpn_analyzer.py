import argparse
from typing import Any

from dns_leak_test import run_dns_leak_test
from ip_check import get_ip_info, print_ip_info
from speed_test import print_speed_results, run_speed_test


def run_full_analysis() -> dict[str, Any]:
    """Run all VPN checks and return collected results."""
    return {
        "ip": get_ip_info(),
        "speed": run_speed_test(),
        "dns": run_dns_leak_test(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="VPN Analyzer Toolkit: IP check, speed test, and DNS leak test"
    )
    parser.add_argument("--ip", action="store_true", help="Run only IP location check")
    parser.add_argument("--speed", action="store_true", help="Run only VPN speed test")
    parser.add_argument("--dns", action="store_true", help="Run only DNS leak test")

    args = parser.parse_args()

    # If no specific flag is given, run everything.
    run_all = not any([args.ip, args.speed, args.dns])

    print("=" * 60)
    print("VPN Analyzer Toolkit")
    print("=" * 60)

    if args.ip or run_all:
        print("\n[1/3] IP Location Detection")
        print_ip_info(get_ip_info())

    if args.speed or run_all:
        print("\n[2/3] VPN Speed Test")
        speed_results = run_speed_test()
        print_speed_results(speed_results)

    if args.dns or run_all:
        print("\n[3/3] DNS Leak Check")
        dns_results = run_dns_leak_test()
        print(f"Configured DNS resolver IP: {dns_results.get('resolver_ip', 'Unknown')}")
        print(f"Resolved test domains: {dns_results.get('resolved_domains', 0)}")
        print(f"Potential issues detected: {dns_results.get('potential_issues', 0)}")
        if dns_results.get("issues"):
            print("Details:")
            for issue in dns_results["issues"]:
                print(f"- {issue}")
        else:
            print("No obvious DNS issues detected by this basic check.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
