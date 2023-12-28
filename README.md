<h1 align="center">
  ArcherX - powerful OSINT-multitool
</h1>

<p align="center">
  <img src="images/archerbanner.png">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/version-1.12.3-red"> <img src="https://img.shields.io/badge/lang-python-blue?logo=python"> <img src="https://img.shields.io/badge/plat-linux-yellow?logo=linux"> <img src="https://img.shields.io/badge/plat-windows-blue?logo=windows"> <img src="https://img.shields.io/badge/license-MIT-green?logo=mit">
</p>


<p align="center">
  <a href="https://github.com/memb3r/archerX/#about">About</a>  ·  <a href="https://github.com/memb3r/archerX/#installation">Installation</a>  ·   <a href="https://github.com/memb3r/archerX/#usage">Usage</a>  ·  <a href="https://github.com/memb3r/archerX/#license">License</a>
</p>


# About

ArcherX - powerful OSINT-multitool with different and useful tools like IP lookup, port scanner, WHOIS lookup and more. Also, ArcherX is a mix of my previous projects like [archer](https://www.github.com/memb3r/archer), [webrover](https://www.github.com/memb3r/webrover) and [ontotool](https://www.github.com/memb3r/ontotool).

> [!WARNING]
> This project was created for entertainment purposes and has no intention of harming anyone.

---

# Installation

### Windows

For running this project you need to install <code>python</code> and <code>pip</code> first.

1. Go to <b>Microsoft Store.</b>

<img src="images/screenshot.png">

2. Click "Get" and install the latest <code>python</code> version (3.12)
3. Download ZIP file of this repo and unpack it.
4. Now go into <b>PowerShell</b> and go into your repository folder using this command:
```bash
cd archerX
```
### Linux (using apt)

1. First, you need to install <code>python3</code>, <code>python3-pip</code>. Open terminal and do this:

```bash
sudo apt install python3 python3-pip
```

2. Now download ZIP file of this repo and unpack it.

>[!TIP]
>You can also use git to download repos faster.
>```bash
>sudo apt install git # Installing git
>
>git clone https://github.com/memb3r/archerX # Cloning repo
>```

3. Go to repo folder:
```bash
cd archerX
```

---

# Usage

Now you need to setup your <b>LeakCheck API</b> if you want to use program fully. You can get your API here - https://wiki.leakcheck.io/ru/api.

Lines with API variables - 493, 533.

After opening the project, it will install libraries automaticly. If you have troubles, you can install libraries automaticly. Libraries list:
```
geopy
phonenumbers
requests
beautifulsoup4
python-whois
```

To open python file, use this (working on Windows and Linux too):
```bash
python3 archerx.py
```

### Commands

- `help` - Show help message.
- `phone` - Phone number lookup. Using phonenumbers library.
- `tg` - Telegram user info. (NOT WORKING)
- `ip` - IP lookup. Using https://ipapi.co free API.
- `github` - GitHub scraper. Using beautifulsoup4 scraping.
- `sub` - Subdomain finder. (NOT WORKING)
- `plate` - Ukraine car plane lookup. (NOT WORKING)
- `user` - Username lookup. Using requests.
- `email` - Email lookup. Using https://leakcheck.net API.
- `whois` - WHOIS domain lookup. Using python-whois free API.
- `faker` - Fake information generator. Using faker generator.
- `port` - Port scanner. Using socket.
- `dip` - Domain to IP. Using socket.
- `ipd` - IP to domain. Using socket.
- `clear` - Clear screen. Only banner stays.

---

# License

This project use [MIT License](LICENSE).
