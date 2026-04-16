import socket


def resolve_domains(subdomains, silent=False):
    valid = []

    for sub in subdomains:
        try:
            socket.gethostbyname(sub)
            valid.append(sub)

            if not silent:
                print(f"[✔] {sub}")
            else:
                print(sub)

        except:
            pass

    return valid