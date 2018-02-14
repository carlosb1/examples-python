# coding=utf-8

import argparse
import os
import sys
import json

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import instabot

try:
    input = raw_input
except NameError:
    pass

def get_media_id_with_location_and_tags(new_bot, new_location, tags):
    media_ids = []
    max_id=''
    if new_bot.getLocationFeed(new_location['location']['pk'], maxid=max_id):
        location_feed = new_bot.LastJson
        print(json.dumps(location_feed))
        print("------------------------")
        for media in new_bot.filter_medias(location_feed["items"][:amount], quiet=True):
            print(str(media))
            #if bot.comment(media, MESSAGE):
            counter += 1
            pbar.update(1)
            if not location_feed.get('next_max_id'):
                return False
            max_id = location_feed['next_max_id']
            
    return media_ids

def comment_location_feed(new_bot, new_location, amount=0):
    counter = 0
    max_id = ''
    with tqdm(total=amount) as pbar:
        while counter < amount:
            if new_bot.getLocationFeed(new_location['location']['pk'], maxid=max_id):
                location_feed = new_bot.LastJson
                import json
                print(json.dumps(location_feed))
                print("------------------------")
                for media in new_bot.filter_medias(location_feed["items"][:amount], quiet=True):
                    print(str(media))
                    #if bot.comment(media, MESSAGE):
                    counter += 1
                    pbar.update(1)
                if not location_feed.get('next_max_id'):
                    return False
                max_id = location_feed['next_max_id']
    return True



### setup parse args

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('tags', type=str, metavar='tag',nargs='+', help='message')
parser.add_argument('message', type=str, nargs='*', help='message')
args = parser.parse_args()


try:
    print(u'comment messages via location and hashtags')
except TypeError:
    sys.stdout = stdout

#TODO improvement add 
bot = Bot()
bot.login(username=args.u, password=args.p)

if not args.message:
    print("It  is necessary to add some message to start the analysis")
    return

if not args.tags or len(args.tags)==0:
    print("It  is necessary to add tags to start the analysis")
    return


location_name = input(u"Write location name:\n").strip()

if not bot.LastJson['items']:
    exit(1)

ncomments = args.amount or input(u"How much comments per location?\n")
ans = True

media_ids=[]
while ans:
    for n, location in enumerate(bot.LastJson["items"], start=1):
        print(u'{0}. {1}'.format(n, location['title']))
    print(u'\n0. Exit\n')
    ans = input(u"What place would you want to choose?\n").strip()
    if ans == '0':
        exit(0)
    try:
        ans = int(ans) - 1
        if ans in range(len(bot.LastJson["items"])):
                #import json
                #print(json.dumps(bot.LastJson["items"]))
                #print("---------------------")
                #print(str(bot.LastJson["items"][ans]))
                #print("#######################")

                get_media_id_with_location_and_tags(bot,bot.LastJson["items"][ans],tags)
    except ValueError:
        print(u"\n Not valid choice. Try again")


