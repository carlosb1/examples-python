import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

default_file_messages = 'example_message.txt'

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-n', type=int, help="amount", default=100)
parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
args = parser.parse_args()



with open(default_file_messages) as f:
    content = f.readlines()

content = [msg.strip() for msg in content]

print("Messages to use")
print(content)

if len(content) == 0:
    print("It is necessary to  include messages to add")
    exit(1)
if args.n <=0:
    print("Add a positive number ")
    exit(1)

if len(args.hashtags) !=2:
    print("It is necessary to work with two hashtags to compare it")
    exit(1)


bot = Bot()
bot.login(username=args.u, password=args.p)

print("Analysing hashtags: "+str(args.hashtags))
print("Number of messages to comment: "+str(args.n))

tag1 = args.hashtags[0]
tag2 = args.hashtags[1]
print("tag1 to compare="+tag1)
print("tag2 to compare="+tag2)

medias = bot.get_total_hashtag_medias(tag1,args.n)

from time import sleep
from random import randint

results_to_comment = []
for media in medias:
    try:
        print("Getting media from:"+str(media))
        text= bot.get_media_info(media)[0]['caption']['text']
        if tag2 in text:
            print("tag="+tag2+"Contain tag:"+text)
            #sleep(randint(1,3))
            results_to_comment.append(media)
    except Exception as e:
        print(str(e))

import datetime, time
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
fil = open('reports_mediaids_'+st+'.txt','w')

import subprocess

for mediaid_to_comment in results_to_comment:
    try:
        message_to_send = content[randint(0,len(content)-1)]
        print("printing message: "+message_to_send+ " to media_id: "+str(mediaid_to_comment))
        sleep(randint(2,5))
        bot.comment(mediaid_to_comment,message_to_send)
        print("Calculating link: ")
        link = subprocess.check_output(['php','id_parser.php',str(mediaid_to_comment)])
        print("link with media:"+str(link))
        fil.write(str(mediaid_to_comment)+","+str(link))
    except Exception as e:
        print(str(e))
        
fil.close()


