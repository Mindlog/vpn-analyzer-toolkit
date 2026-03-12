from dns_leak_test import run_dns_leak_test
from ip_check import get_ip_info
from speed_test import run_speed_test


def main() -> None:
    print("Running example VPN analysis...\n")

    ip_data = get_ip_info()
    print("IP Check:")
    print(ip_data)
    print()

    speed_data = run_speed_test()
    print("Speed Test:")
    print(speed_data)
    print()

    dns_data = run_dns_leak_test()
    print("DNS Leak Test:")
    print(dns_data)


if __name__ == "__main__":
    main()
