import threading
import time
import sys


def clean_domains(subdomains):
    return list(set(subdomains))


def save_to_file(subdomains, filename):
    with open(filename, "w") as f:
        for sub in subdomains:
            f.write(sub + "\n")


# 🔥 Spinner Function
def spinner(stop_event):
    symbols = ["|", "/", "-", "\\"]
    i = 0

    while not stop_event.is_set():
        sys.stdout.write(f"\r[+] Finding subdomains... {symbols[i % len(symbols)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    # Clear line after stopping
    sys.stdout.write("\r" + " " * 60 + "\r")