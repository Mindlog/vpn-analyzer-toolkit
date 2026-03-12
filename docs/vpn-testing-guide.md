# VPN Testing Guide

This guide explains the core methods used by the `vpn-analyzer-toolkit` to evaluate VPN behavior. It is intended as a practical reference for users running local VPN diagnostics.

## 1. Speed Testing

A VPN speed test measures throughput and latency while your VPN tunnel is active.

What is measured:

- Download bandwidth (Mbps)
- Upload bandwidth (Mbps)
- Ping latency (ms)

How it works in this toolkit:

- `speed_test.py` uses `speedtest-cli` to select a nearby test server.
- It performs download and upload tests, then reports summarized metrics.

Why it matters:

- Detects performance overhead introduced by VPN encryption or routing.
- Helps compare VPN servers and protocols.

## 2. DNS Leak Testing

DNS leak testing checks whether DNS requests are going through expected resolvers when VPN is enabled.

How it works in this toolkit:

- `dns_leak_test.py` resolves several known public domains.
- It flags suspicious cases (for example, failure to resolve or private/internal IP responses for public sites).
- It also attempts a resolver-visible public IP check via OpenDNS lookup behavior.

What this basic test can detect:

- Clear resolver errors
- Obvious interception patterns

Limitations:

- This is a basic local check, not a full external DNS leak audit.
- For advanced validation, combine local checks with external DNS leak websites and packet capture tools.

## 3. IP Detection

IP detection verifies the public egress IP and location seen by external services.

How it works in this toolkit:

- `ip_check.py` queries `https://ipinfo.io/json`.
- It returns IP, city, region, country, coordinates, organization, and timezone.

Why it matters:

- Confirms whether VPN exit IP changed from your ISP-provided address.
- Verifies the geographic endpoint expected from the selected VPN server.

## 4. Server Location Analysis

Server location analysis compares expected VPN server location with observed external metadata and speed profile.

Suggested workflow:

1. Connect to a chosen VPN server.
2. Run `python vpn_analyzer.py --ip` and confirm country/city alignment.
3. Run `python vpn_analyzer.py --speed` and record results.
4. Repeat across multiple VPN server regions.
5. Compare latency and throughput to choose the best route.

Interpretation tips:

- Lower ping usually indicates geographically closer routes.
- High download with stable ping often means a healthy VPN path.
- Large performance drops can indicate overloaded or distant VPN gateways.

## Recommended Reference

For VPN comparisons, provider insights, and broader testing context, review:

- https://vpnrating.net/
