#! /usr/bin/env python3
# Br0ther Ey3 OSINT Tool
# @author https://github.com/gsvprharsha

########################################################################################################################################
# NOTE: DO NOT USE THIS TOOL FOR ANY ILLEGAL ACTIVITIES. DEVELOPERS DO NOT TAKE ANY RESPONSIBILITY FOR ANY ILLEGAL USE OF THIS PROGRAM #
########################################################################################################################################

## Imports ##
import argparse
import json
import os
import random
import requests
import sys
import termcolor
import time
from bs4 import BeautifulSoup
from datetime import date
from pytest import UsageError
from useragents import *


## Declaring Arguments ##
def arguments_func():
        parser = argparse.ArgumentParser(description=termcolor.colored("Br0ther Ey3 OSINT Tool v0.0.2","magenta", attrs=['bold']),epilog=termcolor.colored("Embrace The Data :)","green", attrs=['bold']))
        parser.add_argument("--username", help='\t\t'"Profile Username", required=True, nargs=1)
        parser.add_argument("--T10", help="Scans only Top 10 websites from list", required=False, action='store_true')
        parser.add_argument("--fbset",help="Scans the websites owned by Facebook", required=False, action='store_true')
        parser.add_argument("--tiktok","--tt",help="Gather information only on TikTok",required=False, action='store_true')
        parser.add_argument("--tiktok_with_profile_pic","--ttwp", help="\t\t\tTiktok OSINT that also collects the user's profile picture", required=False, action='store_true')
        return parser.parse_args()


## Function to check all the available websites 
def all_dox_function(username):
    print(" ")
    banner()
    print(" ")
    print(termcolor.colored("[+] Looking for: ", "yellow", attrs=['bold']), end=" ")
    print(termcolor.colored(username +  "\n","red", attrs=['bold']))
    time.sleep(0.5)
    print(termcolor.colored('[+] Br0ther_Ey3 v0.0.1 working.......\n',"magenta", attrs=['bold']))
    time.sleep(0.5)

    # INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

    # FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

    #TWITTER
    twitter = f'https://www.twitter.com/{username}'

    # YOUTUBE
    youtube = f'https://www.youtube.com/{username}'

    # BLOGGER
    blogger = f'https://{username}.blogspot.com'

    # GOOGLE+
    google_plus = f'https://plus.google.com/s/{username}/top'

    # REDDIT
    reddit = f'https://www.reddit.com/user/{username}'

    # WORDPRESS
    wordpress = f'https://{username}.wordpress.com'

    # PINTEREST
    pinterest = f'https://www.pinterest.com/{username}'

    # GITHUB
    github = f'https://www.github.com/{username}'

    # TUMBLR
    tumblr = f'https://{username}.tumblr.com'

    # FLICKR
    flickr = f'https://www.flickr.com/people/{username}'

    # STEAM
    steam = f'https://steamcommunity.com/id/{username}'

    # VIMEO
    vimeo = f'https://vimeo.com/{username}'

    # SOUNDCLOUD
    soundcloud = f'https://soundcloud.com/{username}'

    # DISQUS
    disqus = f'https://disqus.com/by/{username}'

    # MEDIUM
    medium = f'https://medium.com/@{username}'

    # DEVIANTART
    deviantart = f'https://{username}.deviantart.com'

    # VK
    vk = f'https://vk.com/{username}'

    # ABOUT.ME
    aboutme = f'https://about.me/{username}'

    # IMGUR
    imgur = f'https://imgur.com/user/{username}'

    # FLIPBOARD
    flipboard = f'https://flipboard.com/@{username}'

    # SLIDESHARE
    slideshare = f'https://slideshare.net/{username}'

    # FOTOLOG
    fotolog = f'https://fotolog.com/{username}'

    # SPOTIFY
    spotify = f'https://open.spotify.com/user/{username}'

    # MIXCLOUD
    mixcloud = f'https://www.mixcloud.com/{username}'

    # SCRIBD
    scribd = f'https://www.scribd.com/{username}'

    # BADOO
    badoo = f'https://www.badoo.com/en/{username}'

    # PATREON
    patreon = f'https://www.patreon.com/{username}'

    # BITBUCKET
    bitbucket = f'https://bitbucket.org/{username}'

    # DAILYMOTION
    dailymotion = f'https://www.dailymotion.com/{username}'

    # ETSY
    etsy = f'https://www.etsy.com/shop/{username}'

    # CASHME
    cashme = f'https://cash.me/{username}'

    # BEHANCE
    behance = f'https://www.behance.net/{username}'

    # GOODREADS
    goodreads = f'https://www.goodreads.com/{username}'

    # INSTRUCTABLES
    instructables = f'https://www.instructables.com/member/{username}'

    # KEYBASE
    keybase = f'https://keybase.io/{username}'

    # KONGREGATE
    kongregate = f'https://kongregate.com/accounts/{username}'

    # LIVEJOURNAL
    livejournal = f'https://{username}.livejournal.com'

    # ANGELLIST
    angellist = f'https://angel.co/{username}'

    # LAST.FM
    last_fm = f'https://last.fm/user/{username}'

    # DRIBBBLE
    dribbble = f'https://dribbble.com/{username}'

    # CODECADEMY
    codecademy = f'https://www.codecademy.com/{username}'

    # GRAVATAR
    gravatar = f'https://en.gravatar.com/{username}'

    # PASTEBIN
    pastebin = f'https://pastebin.com/u/{username}'

    # FOURSQUARE
    foursquare = f'https://foursquare.com/{username}'

    # ROBLOX
    roblox = f'https://www.roblox.com/user.aspx?username={username}'

    # GUMROAD
    gumroad = f'https://www.gumroad.com/{username}'

    # NEWSGROUND
    newsground = f'https://{username}.newgrounds.com'

    # WATTPAD
    wattpad = f'https://www.wattpad.com/user/{username}'

    # CANVA
    canva = f'https://www.canva.com/{username}'

    # CREATIVEMARKET
    creative_market = f'https://creativemarket.com/{username}'

    # TRAKT
    trakt = f'https://www.trakt.tv/users/{username}'

    # 500PX
    five_hundred_px = f'https://500px.com/{username}'

    # BUZZFEED
    buzzfeed = f'https://buzzfeed.com/{username}'

    # TRIPADVISOR
    tripadvisor = f'https://tripadvisor.com/members/{username}'

    # HUBPAGES
    hubpages = f'https://{username}.hubpages.com'

    # CONTENTLY
    contently = f'https://{username}.contently.com'

    # HOUZZ
    houzz = f'https://houzz.com/user/{username}'

    #BLIP.FM
    blipfm = f'https://blip.fm/{username}'

    # WIKIPEDIA
    wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

    # HACKERNEWS
    hackernews = f'https://news.ycombinator.com/user?id={username}'

    # CODEMENTOR
    codementor = f'https://www.codementor.io/{username}'

    # REVERBNATION
    reverb_nation = f'https://www.reverbnation.com/{username}'

    # DESIGNSPIRATION
    designspiration = f'https://www.designspiration.net/{username}'

    # BANDCAMP
    bandcamp = f'https://www.bandcamp.com/{username}'

    # COLOURLOVERS
    colourlovers = f'https://www.colourlovers.com/love/{username}'

    # IFTTT
    ifttt = f'https://www.ifttt.com/p/{username}'

    # EBAY
    ebay = f'https://www.ebay.com/usr/{username}'

    # SLACK
    slack = f'https://{username}.slack.com'

    # OKCUPID
    okcupid = f'https://www.okcupid.com/profile/{username}'

    # TRIP
    trip = f'https://www.trip.skyscanner.com/user/{username}'

    # ELLO
    ello = f'https://ello.co/{username}'

    # TRACKY
    tracky = f'https://tracky.com/user/~{username}'

    # BASECAMP
    basecamp = f'https://{username}.basecamphq.com/login'

    # TWITCH
    twitch = f'https://twitch.tv/{username}'

    WEBSITES = [instagram, facebook, twitter, youtube, blogger, google_plus, reddit, wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify, mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance, goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm, dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground, wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages, contently, houzz, blipfm, wikipedia, hackernews, codementor,reverb_nation, designspiration,bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,]

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        # CHECK FOR STATUS CODE 200; IF EXISTS THEN PRINT THE OUTPUT OF MATCH FOUND; ELSE IF PRINT FALSE POSITIVE IF THE CODE IS 200 AND TEXT WAS NOT FOUND IN URL
        if r.status_code == 200:
            if match == True:
                print(termcolor.colored('[+] FOUND MATCHES','green', attrs=['bold']))
                match = False
            print(termcolor.colored(f'\n{url} - {r.status_code} - OK', 'blue', attrs=['bold']))
            if username in r.text:
                print(termcolor.colored("POSITIVE MATCH CONFIRMED: Username: " + username + " - text detected in url.", "green", attrs=['bold']))
            else:
                print(termcolor.colored("MATCH: Username: " + username + " - But text NOT detected in url, POTENTIAL FALSE POSITIVE.", "red", attrs=['bold']))
                # print('POSITIVE MATCH: Username:{username} - text has NOT been detected in url, could be a FALSE POSITIVE.')#
        count += 1

    total = len(WEBSITES)
    print(termcolor.colored("\nMATCHED: A total of",'yellow'),end=" ")
    print(termcolor.colored(count,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("MATCHES found out of",'yellow'),end=" ")
    print(termcolor.colored(total,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("websites",'yellow'),end=" ")
    sys.exit()
    
## Function to check the TOP 10 websites that have are listed by developers
def T10(username):
    print(" ")
    banner()
    print(" ")
    print(termcolor.colored("[+] Looking for: ", "yellow", attrs=['bold']), end=" ")
    print(termcolor.colored(username +  "\n","red", attrs=['bold']))
    time.sleep(0.5)
    print(termcolor.colored('[+] Br0ther_Ey3 v0.0.1 working.......\n',"magenta", attrs=['bold']))
    time.sleep(0.5)

    # INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

    # FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

    #TWITTER
    twitter = f'https://www.twitter.com/{username}'

    # YOUTUBE
    youtube = f'https://www.youtube.com/{username}'

    # BLOGGER
    blogger = f'https://{username}.blogspot.com'

    # GOOGLE+
    google_plus = f'https://plus.google.com/s/{username}/top'

    # REDDIT
    reddit = f'https://www.reddit.com/user/{username}'

    # PINTEREST
    pinterest = f'https://www.pinterest.com/{username}'

    # GITHUB
    github = f'https://www.github.com/{username}'

    # SPOTIFY
    spotify = f'https://open.spotify.com/user/{username}'

    # TWITCH
    twitch = f'https://twitch.tv/{username}'

    WEBSITES = [instagram, facebook, twitter, youtube, blogger, reddit, twitch, pinterest, github, spotify]

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        # CHECK FOR STATUS CODE 200; IF EXISTS THEN PRINT THE OUTPUT OF MATCH FOUND; ELSE IF PRINT FALSE POSITIVE IF THE CODE IS 200 AND TEXT WAS NOT FOUND IN URL
        if r.status_code == 200:
            if match == True:
                print(termcolor.colored('[+] FOUND MATCHES','green', attrs=['bold']))
                match = False
            print(termcolor.colored(f'\n{url} - {r.status_code} - OK', 'blue', attrs=['bold']))
            if username in r.text:
                print(termcolor.colored("POSITIVE MATCH CONFIRMED: Username: " + username + " - text detected in url.", "green", attrs=['bold']))
            else:
                print(termcolor.colored("MATCH: Username: " + username + " - But text NOT detected in url, POTENTIAL FALSE POSITIVE.", "red", attrs=['bold']))
                # print('POSITIVE MATCH: Username:{username} - text has NOT been detected in url, could be a FALSE POSITIVE.')#
        count += 1

    total = len(WEBSITES)
    print(termcolor.colored("\nMATCHED: A total of",'yellow'),end=" ")
    print(termcolor.colored(count,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("MATCHES found out of",'yellow'),end=" ")
    print(termcolor.colored(total,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("websites",'yellow'),end=" ")
    sys.exit()


def custom_num(username):
    print("custom" + username)
    sys.exit()

## Funtion to check for websites owned by FB
def fbset(username):
    print(" ")
    banner()
    print(" ")
    print(termcolor.colored("[+] Looking for: ", "yellow", attrs=['bold']), end=" ")
    print(termcolor.colored(username +  "\n","red", attrs=['bold']))
    time.sleep(0.5)
    print(termcolor.colored('[+] Br0ther_Ey3 v0.0.1 working.......\n',"magenta", attrs=['bold']))
    time.sleep(0.5)


    # INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

    # FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

    WEBSITES = [instagram, facebook]

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        # CHECK FOR STATUS CODE 200; IF EXISTS THEN PRINT THE OUTPUT OF MATCH FOUND; ELSE IF PRINT FALSE POSITIVE IF THE CODE IS 200 AND TEXT WAS NOT FOUND IN URL
        if r.status_code == 200:
            if match == True:
                print(termcolor.colored('[+] FOUND MATCHES','green', attrs=['bold']))
                match = False
            print(termcolor.colored(f'\n{url} - {r.status_code} - OK', 'blue', attrs=['bold']))
            if username in r.text:
                print(termcolor.colored("POSITIVE MATCH CONFIRMED: Username: " + username + " - text detected in url.", "green", attrs=['bold']))
            else:
                print(termcolor.colored("MATCH: Username: " + username + " - But text NOT detected in url, POTENTIAL FALSE POSITIVE.", "red", attrs=['bold']))
                # print('POSITIVE MATCH: Username:{username} - text has NOT been detected in url, could be a FALSE POSITIVE.')#
        count += 1

    total = len(WEBSITES)
    print(termcolor.colored("\nMATCHED: A total of",'yellow'),end=" ")
    print(termcolor.colored(count,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("MATCHES found out of",'yellow'),end=" ")
    print(termcolor.colored(total,'yellow',attrs=['bold']),end=" ")
    print(termcolor.colored("websites",'yellow'),end=" ")
    sys.exit()


#####################  Tiktok OSINT BEGIN ##################### 
def scrape_profile(username):
    r = requests.get(f'https://tiktok.com/{username}',headers={'User-Agent':random.choice(user_agents)})
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
    content = json.loads(content[0].contents[0])
    print(content["props"]["pageProps"])

    profile_data = {
			"UserID":content["props"]["pageProps"]["userInfo"]["user"]["id"],
			"username":content["props"]["pageProps"]["userInfo"]["user"]["uniqueId"],
			"nickName":content["props"]["pageProps"]["userInfo"]["user"]["nickname"],
			"bio":content["props"]["pageProps"]["userInfo"]["user"]["signature"],
			"profileImage":content["props"]["pageProps"]["userInfo"]["user"]["avatarLarger"],
			"following":content["props"]["pageProps"]["userInfo"]["stats"]["followingCount"],
			"followers":content["props"]["pageProps"]["userInfo"]["stats"]["followerCount"],
			"fans":content["props"]["pageProps"]["userInfo"]["stats"]["followerCount"],
			"hearts":content["props"]["pageProps"]["userInfo"]["stats"]["heart"],
			"videos":content["props"]["pageProps"]["userInfo"]["stats"]["videoCount"],
			"verified":content["props"]["pageProps"]["userInfo"]["user"]["verified"]
            }
    return profile_data

def save_data(username):
    with open(f'{username}_profile_data.json','w') as f:
        f.write(json.dumps(username.data))
    print("Profile data saved to: " + os.getcwd())

def create_dir(username):
    i = 0
    while True:
        try:
            os.mkdir(username)
            os.chdir(username)
            break
        except FileExistsError:
            i += 1

def print_data(username):
    for key,value in username.data.items():
        print(f"{key.upper()}: {value}")

def tiktok_profile_picture(username):
    r = requests.get(username.data['profileImage'])
    with open(f"{username}'.jpg","wb") as f:
        f.write(r.content)

##################### TIKTOK OSINT END #######################
            

####### BANNER ########
def banner():
    the_day = date.today()
    the_time = time.localtime()
    d1 = time.strftime("%H:%M:%S",the_time)
    d2 = the_day.strftime("%B %d, %Y")
    print(termcolor.colored("Starting Br0ther Ey3 on " + d2 + " at " + d1 + "\n"))
    print(termcolor.colored('''\t\t\t\t\t            _ . - = - . _ ''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t       . "  \  \   /  /  " .''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t     ,  \                 /  .''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t   . \   _,.--~=~"~=~--.._   / .''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t  ;  _.-"  / \ !   ! / \  "-._  .''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t / ,"     / ,` .---. `, \     ". \ ''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t/.'   `~  |   /:::::\   |  ~`   '.\\''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t\\`.  `~   |   \:::::/   | ~`  ~ .'/ ''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t \ `.  `~ \ `, `~~~' ,` /   ~`.' /''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t  .  "-._  \ / !   ! \ /  _.-"  .''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t   ./    "=~~.._  _..~~=`"    \.''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t     ,/         ""          \,''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t       . _/             \_ . ''',"magenta", attrs=['bold']))
    print(termcolor.colored('''\t\t\t\t\t          " - ./. .\. - " \n''',"magenta", attrs=['bold']))
    print(termcolor.colored("NOTE: THE LINKS ARE TO BE CHECKED MANUALLY. THE RESULTS ARE ONLY BASED ON THE STATUS CODES OF EACH WEBSITE", 'red', attrs=['bold']))

############# MAIN FUNCTION TO EXECUTE THE DOX FUNCTION ##############
def main():
    args = arguments_func()
    if args.T10 == True:
        T10(args.username[0])
    elif args.username is None:
        print("No arguments")
    elif args.fbset == True:
        fbset(args.username[0])
    elif args.tiktok == True:
        create_dir()
        scrape_profile()
        save_data()
        print_data()
        exit
    elif args.tiktok_with_profile_pic == True:
        create_dir()
        scrape_profile()
        save_data()
        print_data()
        tiktok_profile_picture()
        exit    
    else:
        all_dox_function(args.username[0])
        


#################### IF THE FILE IS RUN; THEN EXECUTE THE main() FUNCTION; IF KEYBOARD INTERRUPT OR TYPE ERROR; THEN EXIT 
if __name__=='__main__':
    try:
        main()
    except UsageError as UE:
        print("Usage Error")
        arguments_func()
    except KeyboardInterrupt as KI:
        print(termcolor.colored("\nInturrupt Recieved.....","red", attrs=['bold']))
        sys.exit()
    except TypeError as TE:
        print("Type Error Recieved")
