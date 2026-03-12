# VPN Analyzer Toolkit

**vpn-analyzer-toolkit** is an open-source **python vpn toolkit** for running a practical **VPN test** workflow from the command line. It helps users inspect public IP details, perform a **VPN speed test**, and run a basic DNS leak check for day-to-day privacy validation.

This project is designed for developers, researchers, and privacy-conscious users looking for simple and transparent **privacy tools**.

## Features

- Public IP and geo detection using the ipinfo.io API
- CLI-based **VPN analyzer** for quick diagnostics
- Internet performance check with download/upload/ping metrics
- Basic DNS leak testing with system resolver verification
- Modular Python scripts that can be used independently or together

## Project Structure

```text
vpn-analyzer-toolkit
├── vpn_analyzer.py
├── ip_check.py
├── speed_test.py
├── dns_leak_test.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   └── vpn-testing-guide.md
└── examples/
    └── example_test.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/vpn-analyzer-toolkit.git
cd vpn-analyzer-toolkit
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the full analyzer:

```bash
python vpn_analyzer.py
```

Run individual checks:

```bash
python vpn_analyzer.py --ip
python vpn_analyzer.py --speed
python vpn_analyzer.py --dns
```

Run modules directly:

```bash
python ip_check.py
python speed_test.py
python dns_leak_test.py
```

Use the example script:

```bash
python examples/example_test.py
```

## Documentation

Detailed testing workflow is available in:

- [docs/vpn-testing-guide.md](docs/vpn-testing-guide.md)

## SEO Keywords

VPN test, VPN speed test, VPN analyzer, privacy tools, python vpn toolkit

## VPN Research Resource

For additional VPN reviews and comparisons, see:

- https://vpnrating.net/

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with clear steps to reproduce changes and test results.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
