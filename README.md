![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/Version-1.0-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub stars](https://img.shields.io/github/stars/Krish-Patwa01/subx?style=social)
![GitHub forks](https://img.shields.io/github/forks/Krish-Patwa01/subx?style=social)

# ⚡ SubX

```
███████╗██╗   ██╗██████╗ ██╗  ██╗
██╔════╝██║   ██║██╔══██╗╚██╗██╔╝
███████╗██║   ██║██████╔╝ ╚███╔╝ 
╚════██║██║   ██║██╔══██╗ ██╔██╗ 
███████║╚██████╔╝██████╔╝██╔╝ ██╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
```

⚡ Smart Subdomain Recon Tool


## 🧠 What is SubX?

**SubX** is a fast and intelligent subdomain discovery tool built for
**penetration testers, bug bounty hunters, and cybersecurity learners**.

It collects subdomains from multiple passive sources and displays only
**valid (live) results** with clean and noise-free output.


## ⚡ Features

* 🔍 Multi-source subdomain discovery
* ⚡ Shows only valid (live) subdomains
* 🧠 Clean & noise-free output
* 🌀 Real-time scanning experience (spinner)
* 📁 Save results to file
* 🔇 Silent mode for automation
* 💻 Beginner-friendly CLI


## ⚙️ Installation

```bash
git clone https://github.com/Krish-Patwa01/subx.git
cd subx
pip install -r requirements.txt
```


##  Usage

```bash
python3 subx.py example.com
```


##  Examples

```bash
# Basic Scan
python3 subx.py example.com

# Save Output
python3 subx.py example.com -o result.txt

# Silent Mode
python3 subx.py example.com --silent
```


## 🖥️ Output Preview

```
[+] Target: example.com
[+] Finding subdomains...

[✔] api.example.com
[✔] mail.example.com
[✔] dev.example.com

[+] Total Valid Subdomains: 3
```


##  Use Cases

* Bug bounty reconnaissance
* OSINT data gathering
* Subdomain enumeration
* Cybersecurity learning


## ⚠️ Disclaimer

This tool is strictly for **educational purposes and authorized testing only**.
Unauthorized usage is illegal.


## ⭐ Support

If you like SubX, give it a ⭐ and share it with the community.


##  Tagline

> Connecting Hacker With Purpose.
