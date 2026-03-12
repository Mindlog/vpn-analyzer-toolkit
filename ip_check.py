from __future__ import annotations

from typing import Any

import requests

IPINFO_URL = "https://ipinfo.io/json"


def get_ip_info() -> dict[str, Any]:
    """Fetch public IP and location metadata from ipinfo.io."""
    try:
        response = requests.get(IPINFO_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        return {"error": f"Failed to query ipinfo.io: {exc}"}

    return {
        "ip": data.get("ip", "Unknown"),
        "city": data.get("city", "Unknown"),
        "region": data.get("region", "Unknown"),
        "country": data.get("country", "Unknown"),
        "location": data.get("loc", "Unknown"),
        "org": data.get("org", "Unknown"),
        "timezone": data.get("timezone", "Unknown"),
    }


def print_ip_info(ip_data: dict[str, Any]) -> None:
    """Print a user-friendly IP information summary."""
    if "error" in ip_data:
        print(ip_data["error"])
        return

    print(f"Public IP: {ip_data['ip']}")
    print(
        "Location: "
        f"{ip_data['city']}, {ip_data['region']}, {ip_data['country']}"
    )
    print(f"Coordinates: {ip_data['location']}")
    print(f"ISP/Organization: {ip_data['org']}")
    print(f"Timezone: {ip_data['timezone']}")


if __name__ == "__main__":
    print_ip_info(get_ip_info())
