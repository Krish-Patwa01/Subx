import requests


def passive_enum(domain):
    subdomains = set()

    # 🔹 crt.sh
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            data = response.json()

            for entry in data:
                names = entry.get("name_value", "").split("\n")

                for sub in names:
                    sub = sub.strip()

                    if domain in sub:
                        subdomains.add(sub)

    except:
        pass

    # 🔹 HackerTarget
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200 and "error" not in response.text.lower():
            for line in response.text.splitlines():
                sub = line.split(",")[0].strip()

                if domain in sub:
                    subdomains.add(sub)

    except:
        pass

    # 🔹 AlienVault
    try:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            data = response.json()

            for entry in data.get("passive_dns", []):
                sub = entry.get("hostname", "").strip()

                if domain in sub:
                    subdomains.add(sub)

    except:
        pass

    return list(subdomains)