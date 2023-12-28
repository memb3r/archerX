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
  1.12.3 (Stable)
</p>

# Content

- [Content](https://github.com/memb3r/archerX/#content)
- [About](https://github.com/memb3r/archerX/#about)
  - [Information](https://github.com/memb3r/archerX/#information)
  - [Preview](https://github.com/memb3r/archerX/#preview)
- [Installation](https://github.com/memb3r/archerX/#installation)
  - [Windows](https://github.com/memb3r/archerX/#windows)
  - [Linux](https://github.com/memb3r/archerX/#linux)
- [Usage](https://github.com/memb3r/archerX/#usage)
  - [APIs](https://github.com/memb3r/archerX/#apis)
  - [Libraries](https://github.com/memb3r/archerX/#libraries)
  - [Commands](https://github.com/memb3r/archerX/#commands)
- [Plans](https://github.com/memb3r/archerX/#plans)
- [Tested on](https://github.com/memb3r/archerX/#tested-on)
- [License](https://github.com/memb3r/archerX/#license)

# About

### Information

ArcherX - powerful OSINT-multitool with different and useful tools like IP lookup, port scanner, WHOIS lookup and more. Also, ArcherX is a mix of my previous projects like [archer](https://www.github.com/memb3r/archer), [webrover](https://www.github.com/memb3r/webrover) and [ontotool](https://www.github.com/memb3r/ontotool).

> [!WARNING]
> This project was created for entertainment purposes and has no intention of harming anyone.

### Preview

<img src="images/preview.png">

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
### Linux

In this example we are using `apt`, that uses in Ubuntu, Debian, Linux Mint, Kali Linux.

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

### APIs

Now you need to setup your <b>LeakCheck API</b> if you want to use program fully. You can get your API here - https://wiki.leakcheck.io/ru/api.

Lines with API variables - 493, 533.

### Libraries

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

# Plans

- [ ] Make all OSINT functions (In progress).
- [X] Make libraries auto-install.
- [ ] Make Google Collab version.
- [ ] Make ArcherX Telegram bot (In progress).
- [ ] Make Replit version.
- [X] Test on Linux
- [X] Test on Windows

# Tested on

ArcherX should work on all apt-based systems.

| OS            | Tested        |
| ------------- | ------------- |
| Ubuntu 12     | True          |
| Windows 11    | True          |
| Other         | False         |

# License

This project use [MIT License](LICENSE).

>MIT License
>
>Copyright (c) 2023 Memb3r
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.
