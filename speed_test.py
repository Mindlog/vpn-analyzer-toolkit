from __future__ import annotations

from typing import Any

import speedtest


def run_speed_test() -> dict[str, Any]:
    """Run a speed test and return ping, download, and upload metrics."""
    try:
        tester = speedtest.Speedtest()
        tester.get_best_server()
        download_bps = tester.download()
        upload_bps = tester.upload(pre_allocate=False)
        server = tester.results.server or {}
        ping = tester.results.ping
    except Exception as exc:  # speedtest can raise multiple runtime exceptions
        return {"error": f"Speed test failed: {exc}"}

    return {
        "download_mbps": round(download_bps / 1_000_000, 2),
        "upload_mbps": round(upload_bps / 1_000_000, 2),
        "ping_ms": round(ping, 2),
        "server": {
            "name": server.get("name", "Unknown"),
            "country": server.get("country", "Unknown"),
            "sponsor": server.get("sponsor", "Unknown"),
        },
    }


def print_speed_results(results: dict[str, Any]) -> None:
    """Print speed test results in CLI-friendly format."""
    if "error" in results:
        print(results["error"])
        return

    print(f"Download: {results['download_mbps']} Mbps")
    print(f"Upload:   {results['upload_mbps']} Mbps")
    print(f"Ping:     {results['ping_ms']} ms")
    server = results["server"]
    print(
        "Server: "
        f"{server['name']} ({server['country']}) - {server['sponsor']}"
    )


if __name__ == "__main__":
    print_speed_results(run_speed_test())
