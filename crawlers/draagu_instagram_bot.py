# coding=utf-8

import argparse
import os
import sys
import json
from time import sleep
from random import randint

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

try:
    input = raw_input
except NameError:
    pass


def extract_media_id_comment(location_feed):
    strJson = json.dumps(location_feed)
    json_data = json.loads(strJson)
    result_texts = []
    if 'ranked_items' in json_data:
        for item in json_data['ranked_items']:
            try:
                text = item['caption']['text']
                media_id = item['caption']['media_id']
                result_texts.append([text,media_id])
            except Exception as e:
                print("error getting text: "+str(e))
                import datetime, time
                st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
                fil = open('dump_rank_'+st+'.json','w')
                fil.write(strJson)
                fil.close()
    if 'items' in json_data:
        for item in json_data['items']:
            try:
                text = item['caption']['text']
                media_id = item['caption']['media_id']
                result_texts.append([text,media_id])
            except Exception as e:
                print("error getting text: "+str(e))
                import datetime, time
                st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
                fil = open('dump_items_'+st+'.json','w')
                fil.write(strJson)
                fil.close()
    return result_texts
    


def get_media_id_with_location_and_tags(new_bot, new_location, tags):
    media_ids = []
    max_id=''
    texts_from_location = []
    if new_bot.getLocationFeed(new_location['location']['pk'], maxid=max_id):
        location_feed = new_bot.LastJson
        text_from_location = extract_media_id_comment(location_feed)
        texts_from_location.extend(text_from_location)
            
    return texts_from_location

def comment_location_feed(new_bot, new_location, amount=0):
    counter = 0
    max_id = ''
    with tqdm(total=amount) as pbar:
        while counter < amount:
            if new_bot.getLocationFeed(new_location['location']['pk'], maxid=max_id):

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
parser.add_argument('tags', type=str, metavar='tag',nargs='+', help='message')
args = parser.parse_args()


try:
    print(u'comment messages via location and hashtags')
except TypeError:
    sys.stdout = stdout

#TODO improvement add 
bot = Bot()
bot.login(username=args.u, password=args.p)

message = 'hello world'
if not args.tags or len(args.tags)==0:
    print("It  is necessary to add tags to start the analysis")
    exit(1)



location_name = input(u"Write location name:\n").strip()


bot.searchLocation(location_name)

if not bot.LastJson['items']:
    exit(1)

ncomments =  int(input(u"How much comments do you want to add?\n"))

if not isinstance(ncomments,int) or ncomments <= 0 :
    print("It is necessary add a positive number")
    exit(1)


print("msg:"+message)
print("tags:"+str(args.tags))
print("location:"+location_name)




def contains_media(lis, fil):
    for x in lis:
        if fil(x):
            return True
    return False


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
        all_info_locations = []
        if ans in range(len(bot.LastJson["items"])):
            pending = ncomments
            tried = 0
            while len(all_info_locations) < ncomments:
                tried+=1
                info_locations = get_media_id_with_location_and_tags(bot,bot.LastJson["items"][ans],args.tags)
                for info in all_info_locations:
                    print(str(info[0].encode('utf-8')))
                    print(str(info[1]))

                locations_to_add = [location for location in info_locations if not contains_media(all_info_locations, lambda compare_loc: compare_loc[1] == location[1])] 
                all_info_locations.extend(locations_to_add)
                pending = pending - len(locations_to_add)
                print("Pending to find %d, waiting for next search, try %d" %(pending, tried)) 
                sleep(randint(60,60*5)) 
        
        print("----------------------_")
        print("\n".join([str(info[0])+", "+str(info[1]) for info in all_info_locations]))

    except ValueError as  e:
        print(u"\n Not valid choice. Try again: "+str(e))


