# 🔥 Reconfire

Modular, async-powered recon engine for bug bounty, red team, and CTF ops.  
Built to scale across 10k+ domains with Redis queueing, httpx probing, nuclei scanning, ffuf brute, and gau scraping.

## ⚡ Features
- 🔁 Async + Redis for 10k+ domains
- 💥 Modular architecture (plug-and-play per phase)
- 🔍 Passive + active recon via subfinder, httpx, gau
- 🔐 Templated vuln scan with nuclei
- 🗂 Fuzzing endpoints with ffuf
- 🧠 Output directory per phase

## 🧰 Tools Used

| Tool        | Role                         |
|-------------|------------------------------|
| `subfinder` | Subdomain enumeration        |
| `httpx`     | Probe for alive + titles     |
| `gau`       | Historical URL grabbing      |
| `nuclei`    | Vulnerability scanning       |
| `ffuf`      | Endpoint brute-forcing       |

## 🚀 Getting Started

```bash
git clone git@github.com:jasidok/reconfire.git
cd reconfire
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

