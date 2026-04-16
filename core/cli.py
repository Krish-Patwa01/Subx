def show_help():
    print("""
SubX — Smart Subdomain Finder 🔍

Usage:
  python main.py <domain> [options]

Example:
  python main.py example.com
  python main.py example.com -o result.txt

Options:
  -o <file>     Save results to file
  --silent      Show only results
  -h, --help    Show this help menu

Description:
  SubX finds valid (live) subdomains of a domain.
  Simple, fast, and beginner-friendly.

Notes:
  • No setup needed — just run 🚀
  • Only valid subdomains are shown
""")