# coding=utf-8
"""
    instabot example

    Workflow:
        Comment medias by location.
"""

import argparse
import codecs
import os
import sys

from tqdm import tqdm

stdout = sys.stdout
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot


try:
    input = raw_input
except NameError:
    pass


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


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-amount', type=str, help="amount")
parser.add_argument('-message', type=str, help="message")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('locations', type=str, nargs='*', help='locations')
args = parser.parse_args()

try:
    print(u'Comment medias by location')
except TypeError:
    sys.stdout = stdout

MESSAGE = args.message or "Hello World!"

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

if args.locations:
    for location in args.locations:
        print(u"Location: {}".format(location))
        bot.searchLocation(location)
        finded_location = bot.LastJson['items'][0]
        if finded_location:
            print(u"Found {}".format(finded_location['title']))

            ncomments = args.amount or input(u"How much comments per location?\n")
            comment_location_feed(bot, finded_location, amount=int(ncomments))
else:
    location_name = input(u"Write location name:\n").strip()
    bot.searchLocation(location_name)
    if not bot.LastJson['items']:
        print(u'Location was not found')
        exit(1)
    ncomments = args.amount or input(u"How much comments per location?\n")
    ans = True
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
                comment_location_feed(bot, bot.LastJson["items"][ans], amount=int(ncomments))
        except ValueError:
            print(u"\n Not valid choice. Try again")
