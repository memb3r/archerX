import os
import sys
import time
import socket

author = "memb3r"
authorurl = "https://github.com/memb3r/"
version = "1.12.3"

links = {
    "2Dimensions": "https://2Dimensions.com/a/{}",
    "7Cups": "https://www.7cups.com/@{}",
    "9GAG": "https://www.9gag.com/u/{}",
    "About.me": "https://about.me/{}",
    "Academia.edu": "https://independent.academia.edu/{}",
    "Alik.cz": "https://www.alik.cz/u/{}",
    "Apple Discussions": "https://discussions.apple.com/profile/{}",
    "Asciinema": "https://asciinema.org/~{}",
    "Ask Fedora": "https://ask.fedoraproject.org/u/{}",
    "AskFM": "https://ask.fm/{}",
    "Audiojungle": "https://audiojungle.net/user/{}",
    "BLIP.fm": "https://blip.fm/{}",
    "Bandcamp": "https://www.bandcamp.com/{}",
    "Bazar.cz": "https://www.bazar.cz/{}/",
    "Behance": "https://www.behance.net/{}",
    "BitBucket": "https://bitbucket.org/{}/",
    "Blogger": "https://{}.blogspot.com",
    "Bookcrossing": "https://www.bookcrossing.com/mybookshelf/{}/",
    "BuyMeACoffee": "https://buymeacoff.ee/{}",
    "BuzzFeed": "https://buzzfeed.com/{}",
    "CNET": "https://www.cnet.com/profiles/{}/",
    "Carbonmade": "https://{}.carbonmade.com",
    "Career.habr": "https://career.habr.com/{}",
    "Championat": "https://www.championat.com/user/{}",
    "Chatujme.cz": "https://profil.chatujme.cz/{}",
    "Chess": "https://www.chess.com/member/{}",
    "CloudflareCommunity": "https://community.cloudflare.com/u/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    "Codepen": "https://codepen.io/{}",
    "Codewars": "https://www.codewars.com/users/{}",
    "ColourLovers": "https://www.colourlovers.com/lover/{}",
    "Contently": "https://{}.contently.com/",
    "Coroflot": "https://www.coroflot.com/{}",
    "Crevado": "https://{}.crevado.com",
    "DEV Community": "https://dev.to/{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Designspiration": "https://www.designspiration.net/{}/",
    "DeviantART": "https://{}.deviantart.com",
    "Discogs": "https://www.discogs.com/user/{}",
    "Discuss.Elastic.co": "https://discuss.elastic.co/u/{}",
    "Disqus": "https://disqus.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Ello": "https://ello.co/{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "EyeEm": "https://www.eyeem.com/u/{}",
    "F3.cool": "https://f3.cool/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "Facebook Groups": "https://www.facebook.com/groups/{}",
    "Fandom": "https://www.fandom.com/u/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Flipboard": "https://flipboard.com/@{}",
    "Football": "https://www.rusfootball.info/user/{}/",
    "FortniteTracker": "https://fortnitetracker.com/profile/all/{}",
    "Freelance.habr": "https://freelance.habr.com/freelancers/{}",
    "Freelancer.com": "https://www.freelancer.com/u/{}",
    "Freesound": "https://freesound.org/people/{}/",
    "Gamespot": "https://www.gamespot.com/profile/{}/",
    "GetMyUni": "https://www.getmyuni.com/user/{}",
    "Giphy": "https://giphy.com/{}",
    "GitHub": "https://www.github.com/{}",
    "GitHub Support Community": "https://github.community/u/{}/summary",
    "GitLab": "https://gitlab.com/{}",
    "Gitee": "https://gitee.com/{}",
    "GoodReads": "https://www.goodreads.com/{}",
    "Gravatar": "http://en.gravatar.com/{}",
    "Gumroad": "https://www.gumroad.com/{}",
    "GunsAndAmmo": "https://forums.gunsandammo.com/profile/{}",
    "GuruShots": "https://gurushots.com/{}/photos",
    "HackTheBox": "https://forum.hackthebox.eu/profile/{}",
    "Hackaday": "https://hackaday.io/{}",
    "HackerOne": "https://hackerone.com/{}",
    "Houzz": "https://houzz.com/user/{}",
    "HubPages": "https://hubpages.com/@{}",
    "ICQ": "https://icq.im/{}",
    "IFTTT": "https://www.ifttt.com/p/{}",
    "ImgUp.cz": "https://imgup.cz/{}",
    "Instagram": "https://instagram.com/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "Issuu": "https://issuu.com/{}",
    "Itch.io": "https://{}.itch.io/",
    "Jimdo": "https://{}.jimdosite.com",
    "Kaggle": "https://www.kaggle.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Kik": "https://kik.me/{}",
    "Kongregate": "https://www.kongregate.com/accounts/{}",
    "LOR": "https://www.linux.org.ru/people/{}/profile",
    "Launchpad": "https://launchpad.net/~{}",
    "LeetCode": "https://leetcode.com/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Likee": "https://likee.com/@{}",
    "LiveJournal": "https://{}.livejournal.com",
    "Lobsters": "https://lobste.rs/u/{}",
    "Medium": "https://medium.com/@{}",
    "Memrise": "https://www.memrise.com/user/{}/",
    "Munzee": "https://www.munzee.com/m/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "MyMiniFactory": "https://www.myminifactory.com/users/{}",
    "Myspace": "https://myspace.com/{}",
    "NameMC (Minecraft.net skins)": "https://namemc.com/profile/{}",
    "Naver": "https://blog.naver.com/{}",
    "Newgrounds": "https://{}.newgrounds.com",
    "NotABug.org": "https://notabug.org/{}",
    "OK": "https://ok.ru/{}",
    "OpenStreetMap": "https://www.openstreetmap.org/user/{}",
    "Opensource": "https://opensource.com/users/{}",
    "PCPartPicker": "https://pcpartpicker.com/user/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Periscope": "https://www.periscope.tv/{}/",
    "Pinkbike": "https://www.pinkbike.com/u/{}/",
    "PlayStore": "https://play.google.com/store/apps/developer?id={}",
    "Plug.DJ": "https://plug.dj/@/{}",
    "Pokémon Showdown": "https://pokemonshowdown.com/users/{}",
    "Polygon": "https://www.polygon.com/users/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "PromoDJ": "http://promodj.com/{}",
    "PyPi": "https://pypi.org/user/{}",
    "Quizlet": "https://quizlet.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Raidforums": "https://raidforums.com/User-{}",
    "Rajce.net": "https://{}.rajce.idnes.cz/",
    "RapidAPI": "https://rapidapi.com/users/{}",
    "Rate Your Music": "https://rateyourmusic.com/~{}",
    "Redbubble": "https://www.redbubble.com/people/{}",
    "Repl.it": "https://repl.it/@{}",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "RubyGems": "https://rubygems.org/profiles/{}",
    "Sbazar.cz": "https://www.sbazar.cz/{}",
    "Scratch": "https://scratch.mit.edu/users/{}",
    "Scribd": "https://www.scribd.com/{}",
    "ShitpostBot5000": "https://www.shitpostbot.com/user/{}",
    "Signal": "https://community.signalusers.org/u/{}",
    "Slack": "https://{}.slack.com",
    "Slashdot": "https://slashdot.org/~{}",
    "SlideShare": "https://slideshare.net/{}",
    "Snapchat": "https://snapchat.com/add/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "SourceForge": "https://sourceforge.net/u/{}",
    "Speedrun.com": "https://speedrun.com/user/{}",
    "Splits.io": "https://splits.io/users/{}",
    "Sporcle": "https://www.sporcle.com/user/{}/people",
    "SportsRU": "https://www.sports.ru/profile/{}/",
    "Spotify": "https://open.spotify.com/user/{}",
    "Star Citizen": "https://robertsspaceindustries.com/citizens/{}",
    "SublimeForum": "https://forum.sublimetext.com/u/{}",
    "Tellonym.me": "https://tellonym.me/{}",
    "Test PyPi": "https://test.pypi.org/user/{}",
    "TikTok": "https://tiktok.com/@{}",
    "Ultimate-Guitar": "https://ultimate-guitar.com/u/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "VK": "https://vk.com/{}",
    "VSCO": "https://vsco.co/{}",
    "Venmo": "https://venmo.com/{}",
    "Vero": "https://vero.co/{}",
    "Vimeo": "https://vimeo.com/{}",
    "VirusTotal": "https://www.virustotal.com/ui/users/{}/trusted_users",
    "Warrior Forum": "https://www.warriorforum.com/members/{}.html",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "We Heart It": "https://weheartit.com/{}",
    "WebNode": "https://{}.webnode.cz/",
    "Whonix Forum": "https://forums.whonix.org/u/{}",
    "Wikipedia": "https://www.wikipedia.org/wiki/User:{}",
    "Windy": "https://community.windy.com/user/{}",
    "Wix": "https://{}.wix.com",
    "WordPressOrg": "https://profiles.wordpress.org/{}/",
    "Xbox Gamertag": "https://xboxgamertag.com/search/{}",
    "YouPic": "https://youpic.com/photographer/{}/",
    "YouTube": "https://www.youtube.com/{}",
    "Zhihu": "https://www.zhihu.com/people/{}",
    "Akniga": "https://akniga.org/profile/{}",
    "AllMyLinks": "https://allmylinks.com/{}",
    "AminoApp": "https://aminoapps.com/u/{}",
    "authorSTREAM": "http://www.authorstream.com/{}/",
    "babyRU": "https://www.baby.ru/u/{}/",
    "chaos.social": "https://chaos.social/@{}",
    "CouchSurfing": "https://www.couchsurfing.com/people/{}",
    "d3RU": "https://d3.ru/user/{}/posts",
    "Dailykos": "https://www.dailykos.com/user/{}",
    "datingRU": "http://dating.ru/{}",
    "Drive2": "https://www.drive2.ru/users/{}",
    "eGPU": "https://egpu.io/forums/profile/{}/",
    "Eintracht": "https://community.eintracht.de/fans/{}",
    "Fixya": "https://www.fixya.com/users/{}",
    "FL": "https://www.fl.ru/users/{}",
    "GeoCaching": "https://www.geocaching.com/p/default.aspx?u={}",
    "Habr": "https://habr.com/ru/users/{}",
    "Hackster": "https://www.hackster.io/{}",
    "irecommend": "https://irecommend.ru/users/{}",
    "Jeuxvideo": "http://www.jeuxvideo.com/profil/{}?mode=infos",
    "Kofi": "https://ko-fi.com/{}",
    "kwork": "https://kwork.ru/user/{}",
    "Last.fm": "https://last.fm/user/{}",
    "LeaseHackr": "https://forum.leasehackr.com/u/{}/summary/",
    "LiveLib": "https://www.livelib.ru/reader/{}",
    "mastodon.cloud": "https://mastodon.cloud/@{}",
    "mastodon.social": "https://mastodon.social/@{}",
    "Mercadolivre": "https://www.mercadolivre.com.br/perfil/{}",
    "Moikrug": "https://moikrug.ru/{}",
    "Mstdn.io": "https://mstdn.io/@{}",
    "Nairaland.com": "https://www.nairaland.com/{}",
    "nnRU": "https://{}.www.nn.ru/",
    "Note": "https://note.com/{}",
    "npm": "https://www.npmjs.com/~{}",
    "Opennet": "https://www.opennet.ru/~{}",
    "Osu!": "https://osu.ppy.sh/users/{}",
    "satsisRU": "https://satsis.info/user/{}",
    "social.tchncs.de": "https://social.tchncs.de/@{}",
    "Svidbook": "https://www.svidbook.ru/user/{}",
    "uid": "http://uid.me/{}"
}

def banner():
    print('''\u001b[34m                                                       
                                    88                                   
                                    88                                   
                                    88                                   
,adPPYYba,  8b,dPPYba,   ,adPPYba,  88,dPPYba,    ,adPPYba,  8b,dPPYba,  
""     `Y8  88P'   "Y8  a8"     ""  88P'    "8a  a8P_____88  88P'   "Y8  
,adPPPPP88  88          8b          88       88  8PP"""""""  88          
88,    ,88  88          "8a,   ,aa  88       88  "8b,   ,aa  88    
`"8bbdP"Y8  88           `"Ybbd8"'  88       88   `"Ybbd8"'  88  \u001b[37mSetup''')

def banner2():
    print('''\u001b[34m                                                       
                                    88                                   
                                    88                                   
                                    88                                   
,adPPYYba,  8b,dPPYba,   ,adPPYba,  88,dPPYba,    ,adPPYba,  8b,dPPYba,  
""     `Y8  88P'   "Y8  a8"     ""  88P'    "8a  a8P_____88  88P'   "Y8  
,adPPPPP88  88          8b          88       88  8PP"""""""  88          
88,    ,88  88          "8a,   ,aa  88       88  "8b,   ,aa  88    
`"8bbdP"Y8  88           `"Ybbd8"'  88       88   `"Ybbd8"'  88  \u001b[37mX''')

def loading_animation():
    print('''\u001b[34m
    _       _            
   /_\  _ _| |_  ___ _ _ 
  / _ \| '_| ' \/ -_) '_|
 /_/ \_\_| |_||_\___|_| x           
''')
    bar_length = 20
    for i in range(bar_length + 1):
        time.sleep(0.1)
        progress = i / bar_length
        status_bar = "\u001b[34m[\u001b[37m{: <20}\u001b[34m] \u001b[37m{:.0%}\u001b[0m".format("=" * i, progress)
        sys.stdout.write("\r" + status_bar)
        sys.stdout.flush()
    time.sleep(1)
    os.system('clear')

loading_animation()

banner()
try:
    import json
    from geopy.geocoders import Nominatim
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    import requests
    from bs4 import BeautifulSoup
    from whois import whois
except ImportError:
    print('\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSome libraries are missing. Installing...')
    os.system('pip install geopy phonenumbers requests beautifulsoup4 python-whois')
    print('\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mLibraries installed successfully.')
else:
    print('\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mAll required libraries are already installed.')

def main():
    banner2()
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mVersion: {version}')
    print(f'\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mAuthor: {author}')
    print(f'\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mType \u001b[44m"help"\u001b[0m for help.')

    while True:
        command = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType command \u001b[44mhere\u001b[0m: ')
        if (command == 'help'):
            print('\n\u001b[34mBuilt-in commands\u001b[37m:')
            print(f'\u001b[34m[\u001b[37mhelp\u001b[34m]    \u001b[37mShow this help message.') 
            print(f'\u001b[34m[\u001b[37mphone\u001b[34m]   \u001b[37mPhone number lookup.') 
            print(f'\u001b[34m[\u001b[37mtg\u001b[34m]      \u001b[37mTelegram user info. (NOT WORKING)')
            print(f'\u001b[34m[\u001b[37mip\u001b[34m]      \u001b[37mIP lookup.') 
            print(f'\u001b[34m[\u001b[37mgithub\u001b[34m]  \u001b[37mGitHub scraper.') 
            print(f'\u001b[34m[\u001b[37msub\u001b[34m]     \u001b[37mSubdomain finder. (NOT WORKING)')
            print(f'\u001b[34m[\u001b[37mplate\u001b[34m]   \u001b[37mUkraine car plane lookup. (NOT WORKING)')
            print(f'\u001b[34m[\u001b[37muser\u001b[34m]    \u001b[37mUsername lookup.') 
            print(f'\u001b[34m[\u001b[37memail\u001b[34m]   \u001b[37mEmail lookup.') 
            print(f'\u001b[34m[\u001b[37mwhois\u001b[34m]   \u001b[37mWHOIS domain lookup.') 
            print(f'\u001b[34m[\u001b[37mfaker\u001b[34m]   \u001b[37mFake information generator.') 
            print(f'\u001b[34m[\u001b[37mport\u001b[34m]    \u001b[37mPort scanner.') 
            print(f'\u001b[34m[\u001b[37mdip\u001b[34m]     \u001b[37mDomain to IP.') 
            print(f'\u001b[34m[\u001b[37mipd\u001b[34m]     \u001b[37mIP to domain.') 
            print(f'\u001b[34m[\u001b[37mclear\u001b[34m]   \u001b[37mClear screen.') 
        elif (command == ''):
            pass
        elif (command == 'github'):
            githubuser = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType GitHub username \u001b[44mhere\u001b[0m: ')
            if githubuser == '':
                pass
            else:
                githubprofile = "https://github.com/" + githubuser
                req = requests.get(githubprofile)
                scraper = BeautifulSoup(req.content, "html.parser")
                name = scraper.find("span", {"itemprop": "name"}) 
                name_strip = name.text.strip() if name else None
                profile_picture = scraper.find("img", {"width": "260"})
                pfp = profile_picture["src"] if profile_picture else None
                usernamee = scraper.find("span", {"itemprop": "additionalName"})
                usernameee = usernamee.text.strip() if usernamee else None
                desc = scraper.find("div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"})
                description = desc.text.strip() if desc else None
                emoji = scraper.find("div", {"class": "user-status-emoji-container flex-shrink-0 mr-2 d-flex flex-items-center flex-justify-center"})
                emojistatus = emoji.text.strip() if emoji else None
                folls = scraper.find_all("span", {"class": "text-bold color-fg-default"})
                followers = folls[0].text.strip() if folls else None
                following = folls[1].text.strip() if folls else None
                readme = scraper.find("div", {"class": "Box-body p-4"})
                readmeexist = True if readme else False
                loc = scraper.find("span", {"class": "p-label"})
                location = loc.text.strip() if loc else None
                print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mName: {name_strip}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mUsername: {usernameee}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mProfile picture URL: {pfp}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mDescription: {description}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mEmoji status: {emojistatus}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mFollowers: {followers}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mFollowing: {following}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mREADME Exist: {readmeexist}')
                print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLocation: {location}')
        elif (command == 'clear'):
            os.system('clear')
            banner2()
            print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mVersion: {version}')
            print(f'\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mAuthor: {author}')
            print(f'\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mType \u001b[44m"help"\u001b[0m for help.')
        elif (command == 'phone'):
            phonee()
        elif (command == 'email'):
            emaill()
        elif (command == 'user'):
            usernamm()
        elif (command == 'ip'):
            iplook()
        elif (command == 'whois'):
            whoislookup()
        elif (command == 'ipd'):
            iptodomain()
        elif (command == 'dip'):
            domaintoip()
        elif (command == 'port'):
            portscan()
        elif (command == 'faker'):
            fakeinfo()
        else:
            pass

def fakeinfo():
    fake = Faker()
    print(f"\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mFake full name: {fake.name()}")
    print(f"\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mFake address: {fake.address()}")
    print(f"\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mFake text: {fake.text()}")

def portscan():
    target = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType IP \u001b[44mhere\u001b[0m: ')
    if (target == ''):
        return
    try:
        start_port = int(input('\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mEnter the port from which we will start: '))
    except ValueError:
        return
    try:
        end_port = int(input('\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mEnter the port from which we will end: '))
    except ValueError:
        return
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((target, port))
            print('\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mPort ' + str(port) + ' is open')
            s.close()
        except:
            pass

def domaintoip():
    domain = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType domain \u001b[44mhere\u001b[0m: ')
    if (domain == ''):
        return
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return "\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mInvalid domain."
    print(f"\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mThe IP address for {domain} is {ip}")

def iptodomain():
    ip = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType IP \u001b[44mhere\u001b[0m: ')
    if (ip == ''):
        return
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        try:
            domain = socket.gethostbyaddr(socket.gethostbyname(socket.gethostbyaddr(ip)[0]))[0]
        except (socket.herror, socket.gaierror):
            print('\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mNo domain associated with this IP.')
    print('\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mDomain: ' + domain)

def whoislookup():
    domain = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType domain or IP \u001b[44mhere\u001b[0m: ')
    if (domain == ''):
        return
    try:
        w = whois(domain)
        print(w)
    except socket.gaierror:
        print("\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mInvalid domain name")
    except Exception as e:
        print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mError: {e}")

def iplook():
    ipinp = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType IP \u001b[44mhere\u001b[0m: ')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching leaks...')
    if (ipinp == ''):
        return
    request_url = f'https://ipapi.co/{ipinp}/json/'
    try:
        headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
        response = requests.get(request_url, headers=headers)
        if response.status_code == 200:
            ipvalues = response.json()
            print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mIP: {ipinp}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mNetwork: {ipvalues["network"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mVersion: {ipvalues["version"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCity: {ipvalues["city"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mRegion: {ipvalues["region"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mRegion Code: {ipvalues["region_code"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry: {ipvalues["country"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Name: {ipvalues["country_name"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Code: {ipvalues["country_code"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Code ISO3: {ipvalues["country_code_iso3"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Capital: {ipvalues["country_capital"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry TLD: {ipvalues["country_tld"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mContinent Code: {ipvalues["continent_code"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mIn Europe: {ipvalues["in_eu"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mPostal: {ipvalues["postal"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLatitude: {ipvalues["latitude"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLongitude: {ipvalues["longitude"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mTimezone: {ipvalues["timezone"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mUTC Offset: {ipvalues["utc_offset"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Phone Code: {ipvalues["country_calling_code"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCurrency: {ipvalues["currency"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCurrency Name: {ipvalues["currency_name"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLanguages: {ipvalues["languages"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Area: {ipvalues["country_area"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry Population: {ipvalues["country_population"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mASN: {ipvalues["asn"]}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mOrganisation: {ipvalues["org"]}')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status: {response.status_code}. Failed to fetch data from ipapi.co.')
            return
    except requests.exceptions.SSLError as e:
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mSSL Error: {e}')
    except KeyError as e:
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed to fetch {e}. Invalid IP.')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching information on whatismyipaddress.com...')
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mwhatismyipaddress.com URL: https://whatismyipaddress.com/ip/{ipinp}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching geolocation...')
    ipgeolocation = f'{ipvalues["latitude"]}+{ipvalues["longitude"]}'
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mGoogle Maps URL: https://www.google.com/maps/search/{ipgeolocation}')
    geolocator = Nominatim(user_agent="Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    location = geolocator.reverse(f'{ipvalues["latitude"]}, {ipvalues["longitude"]}')
    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mAddress: {location.address}')

def usernamm():
    eusername = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType username \u001b[44mhere\u001b[0m: ')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching leaks...')
    if (eusername == ''):
        return
    leakcheckapi = '' # Enter API here or inside Archer Reborn.
    if leakcheckapi == '':
        leakcheckapiinput = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType LeakCheck API \u001b[44mhere\u001b[0m: ')
        if leakcheckapiinput == '':
            print('\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mThis is not an API.')
            return
        else:
            leakcheckapi = leakcheckapiinput
    url = f"https://leakcheck.net/api/public?key={leakcheckapi}&check=" + eusername
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get("success", False):
            print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mSuccess: {data["success"]}\n')
            sources = data.get("sources", [])
            for source in sources:
                name = source.get("name")
                if name:
                    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLeak name: {name}')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mLeaks are not found! It can be when your email has no leaks or you input invalid LeakCheck API. Get your API here: \u001b[34mhttps://https://wiki.leakcheck.io/en/api\u001b[37m.')
    else:
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}. It can be when you have bad connection or you do email lookup many times. Take a break.')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching all social media...\n')
    results = {}
    for networks, url_templates in links.items():
        full_urls = url_templates.format(eusername)
        response = requests.get(full_urls)
        if response.status_code == 200:
            time.sleep(0.1)
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37m{networks}: {full_urls}')
            results[networks] = full_urls
    if not results:
        print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mSocial media accounts by {eusername} are not found.")

def emaill():
    emailla = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType email \u001b[44mhere\u001b[0m: ')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching leaks...')
    if (emailla == ''):
        return
    leakcheckapi = '' # Enter API here or inside Archer Reborn.
    if leakcheckapi == '':
        leakcheckapiinput = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType LeakCheck API \u001b[44mhere\u001b[0m: ')
        if leakcheckapiinput == '':
            print('\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mThis is not an API.')
            return
        else:
            leakcheckapi = leakcheckapiinput
    url = f"https://leakcheck.net/api/public?key={leakcheckapi}&check=" + emailla
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get("success", False):
            print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mSuccess: {data["success"]}\n')
            sources = data.get("sources", [])
            for source in sources:
                name = source.get("name")
                if name:
                    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mLeak name: {name}')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mLeaks are not found! It can be when your email has no leaks or you input invalid LeakCheck API. Get your API here: \u001b[34mhttps://https://wiki.leakcheck.io/en/api\u001b[37m.')
    else:
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}. It can be when you have bad connection or you do email lookup many times. Take a break.')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching domain names...')
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mURL: https://viewdns.info/reversewhois/?q={emailla}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching basic info...')
    eusername, edomain = emailla.split("@")
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mUsername: {eusername}')
    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mDomain: {edomain}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching in BkRu...')
    mainurl = 'https://my.mail.ru/bk.ru/' + eusername
    response = requests.get(mainurl)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_element = soup.find("h1", itemprop="name")
        if h1_element:
            text = h1_element.text
            print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mName: {text}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mProfile URL: {mainurl}')
        else:
            print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed searching name.")
    else:
        print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}")
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching in InboxRu...')
    mainurl2 = 'https://my.mail.ru/inbox.ru/' + eusername
    response = requests.get(mainurl2)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_element = soup.find("h1", itemprop="name")
        if h1_element:
            text = h1_element.text
            print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mName: {text}')
            print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mProfile URL: {mainurl2}')
        else:
            print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed searching name.")
    else:
        print(f"\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}")

def phonee():
    phonenum = input('\n\u001b[34m[\u001b[37m...\u001b[34m] \u001b[37mType phone number \u001b[44mhere\u001b[0m: ')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching basic information...')
    if (phonenum == ''):
        return
    try:
        parsed_number = phonenumbers.parse(phonenum, None)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        region = phonenumbers.region_code_for_number(parsed_number)
        country = geocoder.description_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)
        carriers = carrier.name_for_number(parsed_number, "en")
    except phonenumbers.NumberParseException:
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mInvalid number. Example: +79998887766.')
        return
    if (is_valid == False):
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mValid: {is_valid}')
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mValid: {is_valid}')
    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mCountry: {country}')
    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mTimezone: {timezones}')
    print(f'\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mOperator: {carriers}')
    if (phonenum.startswith('+380')):
        formattednum = phonenum[1:]
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {formattednum} on ktozvonil.net...')
        tdurl = "https://ktozvonil.net/nomer/" + formattednum
        response = requests.get(tdurl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            count_comments = soup.find("div", itemprop="reviewBody")
            try:
                print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mReview: {count_comments.text}')
            except AttributeError:
                print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed searching review about number on ktozvonil.net.')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}')
        formattednum2 = phonenum[3:]
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {formattednum} on ktozvonit.com.ua...')
        print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mNumber on ktozvonit.com.ua: https://ktozvonit.com.ua/nomer/{formattednum2}')
    if (phonenum.startswith('+7')):
        formattednum = phonenum[2:]
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {formattednum} on netrubi.ru...')
        nturl = "https://netrubi.ru/nomer/" + formattednum
        response = requests.get(nturl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            revieww = soup.find("div", itemprop="description")
            try:
                print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mReview: {revieww.text}')
            except AttributeError:
                print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed searching reviews count number on netrubi.ru.')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}')
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {formattednum} on getscam.com...')
        formattednum2 = phonenum[1:]
        print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mNumber on getscam.com: https://getscam.com/{formattednum2}')
        print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {formattednum} on mysmsbox.ru...')
        msmurl = "https://mysmsbox.ru/phone-search/" + formattednum2
        response = requests.get(msmurl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            reviewww = soup.find("span", class_="color-grey")
            try:
                print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mReview: {reviewww.text}')
            except AttributeError:
                print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mFailed searching reviews count number on mysmsbox.ru.')
        else:
            print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}')
    formattednum3 = phonenum[1:]
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {phonenum} on Telegram...')
    teleurl = 'https://t.me/' + phonenum
    response = requests.get(teleurl)
    if response.status_code == 200:
        print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mTelegram URL: {teleurl}')
    else:
        print(f'\n\u001b[34m[\u001b[37mx\u001b[34m] \u001b[37mResponse status code: {response.status_code}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {phonenum} on Skype...')
    skypeurl = f'skype:{phonenum}?chat'
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mSkype URL: {skypeurl}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {phonenum} on Viber...')
    viberurl = f'viber://chat?number={formattednum3}/'
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mViber URL: {viberurl}')
    print(f'\n\u001b[34m[\u001b[37m!\u001b[34m] \u001b[37mSearching {phonenum} on WhatsApp...')
    whaurl = f'https://wa.clck.bar/{formattednum3}?text=%D0%92%D1%8B%20%D0%B7%D0%B2%D0%BE%D0%BD%D0%B8%D0%BB%D0%B8%20%D0%BC%D0%BD%D0%B5?'
    print(f'\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mWhatsApp URL: {whaurl}')

if __name__ == '__main__':
    main()