import sys
import threading

from core.passive import passive_enum
from core.resolver import resolve_domains
from core.utils import clean_domains, save_to_file, spinner
from core.cli import show_help


def banner():
    print("\n[ SubX v0.2 - Smart Subdomain Finder ]\n")


def main():
    # Help menu
    if "-h" in sys.argv or "--help" in sys.argv:
        show_help()
        sys.exit()

    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    banner()

    domain = sys.argv[1]
    output_file = None
    silent = False

    # Options
    if "-o" in sys.argv:
        try:
            output_file = sys.argv[sys.argv.index("-o") + 1]
        except IndexError:
            print("[-] Output file not specified")
            sys.exit()

    if "--silent" in sys.argv:
        silent = True

    if not silent:
        print(f"[+] Target: {domain}")

    # 🔥 Spinner start
    if not silent:
        stop_event = threading.Event()
        spin_thread = threading.Thread(target=spinner, args=(stop_event,))
        spin_thread.start()

    # Step 1: Passive enumeration
    subdomains = passive_enum(domain)

    # Stop spinner
    if not silent:
        stop_event.set()
        spin_thread.join()
        print("[+] Subdomain search completed!\n")

    # Step 2: Clean duplicates
    subdomains = clean_domains(subdomains)

    if not silent:
        print("[+] Verifying live subdomains...\n")

    # Step 3: Resolve valid domains
    valid_subdomains = resolve_domains(subdomains, silent)

    # Step 4: Save output
    if output_file:
        save_to_file(valid_subdomains, output_file)
        if not silent:
            print(f"\n[✓] Saved to {output_file}")

    # Final count
    if not silent:
        print(f"\n[+] Total Valid Subdomains: {len(valid_subdomains)}")


if __name__ == "__main__":
    main()
