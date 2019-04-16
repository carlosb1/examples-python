# from  openpyxl import Workbook

def get_break(title="Registration", slot_time="09:00 - 09:25", avatar=""):
    if avatar != "":
        avatar = '<div class="sc-avatar-wrapper">' + '\n' + '<img src="' + avatar + '" /></div>'
    result = '<article class="post-wrap" data-animation="fadeInUp" data-animation-delay="300">'\
    '\n' + '    <div class="media">' \
    '\n' + '        <div class="schedule-width">' \
    '\n' + '            <div class="post-header">' \
    '\n' + '                <div class="post-meta">'\
    '\n' + '                    <span class="post-date"><i class="fa fa-clock-o"></i> ' + slot_time + '</span>'\
    '\n' + '                </div>'\
    '\n' + '                <h2 class="post-title">' + title + '</h2>'\
    '\n' + '            </div>'\
    '\n' + '            <div class="post-body">'\
    '\n' + '                <div class="post-excerpt">'\
    '\n' + '                    <br/>'\
    '\n' + '                </div>'\
    '\n' + '            </div>' + avatar + ""\
    '\n' + '        </div>'\
    '\n' + '    </div></article>'
    return result


def get_talk(title, body, authors, twitter_links, avatar_links, slot_time="9:00 - 9:25"):
    info_twitter = ''
    info_avatar = ''
    for index in range(0, len(twitter_links)):
        twitter_link = twitter_links[index]
        author = authors[index]
        avatar_link = avatar_links[index]
        info_twitter += '<a href="' + twitter_link + '"><i class="fa fa-twitter"></i>' + author + '\n</a>'
        info_avatar += '<div class="sc-avatar-wrapper"><img src="' + avatar_link + '" /></div>'

    info_authors = '<div class="post-footer">'\
    '\n' + '                <span class="post-readmore">' + info_twitter + ''\
    '\n' + '                </span>'\
    '\n' + '            </div>' + info_avatar

    result = '<article class="post-wrap" data-animation="fadeInUp" data-animation-delay="300">'\
    '\n' + '    <div class="media">'\
    '\n' + '        <div class="schedule-width">'\
    '\n' + '            <div class="post-header">'\
    '\n' + '                <div class="post-meta">'\
    '\n' + '                    <span class="post-date"><i class="fa fa-clock-o"></i> ' + slot_time + '</span>'\
#                                                               <img class="language-flag" src="assets/img/gb.svg" />
    '\n' + '                    <h2 class="post-title">' + title + '</h2>'\
    '\n' + '                </div>'\
    '\n' + '            </div>'\
    '\n' + '            <div class="post-body">'\
    '\n' + '                <div class="post-excerpt">'\
    '\n' + '                    <p>' + body + ''\
    '\n' + '                    </p>'\
    '\n' + '                </div>'\
    '\n' + '            </div>' + info_authors + ''\
    '\n' + '        </div>'\
    '\n' + '    </div>'\
    '</article>'
    return result


import bs4
if __name__ == '__main__':
    template_file = 'template_schedule.html'

    with open(template_file) as f:
        txt = f.read()
        soup = bs4.BeautifulSoup(txt)
        # REGISTRATION
        # OPENING
        # TALK 1
        # BREAK
        # TALK 2
        # TALK 3
        # LUNCH
        # OPEN SPACE
        # BREAK
        # OPEN SPACE
        # CLOSING
        # wb = Workbook()
        # wb = wb.active()

        # def get_talk(title, body, authors, twitter_links, avatar_links, slot_time="9:00 - 9:25"):
        talks_day1_track1 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]
        talks_day1_track2 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]

        talks_day1_track3 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]
        
        talks_day1_track4 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]

        talks_day2_track1 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]
        talks_day2_track2 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]

        talks_day2_track3 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]
        talks_day2_track4 = [get_break(), get_break(title="Opening"),\
                get_talk("talk1", "title1", ["author1"], ["twitter_link1"], ["avatar_link1"]),\
                get_break(title="Break"),\
                get_talk("talk2", "title2", ["author2"], ["twitter_link2"], ["avatar_link2"]),\
                get_talk("talk3", "title3", ["author3"], ["twitter_link3"], ["avatar_link3"]),\
                get_break(title="Lunch"),\
                get_break(title="OpenSpace"),\
                get_break(title="Break"),\
                get_break(title="OpenSpace"),\
                get_break(title="Closing"),\
        ]


        day1_track1 = soup.find('div', id='tab-lv21-first').find('div', class_='timeline')
        [day1_track1.append(talk) for talk in talks_day1_track1]


        day1_track2 = soup.find('div', id='tab-lv21-second').find('div', class_='timeline')
        [day1_track2.append(talk) for talk in talks_day1_track2]

        day1_track3 = soup.find('div', id='tab-lv21-third').find('div', class_='timeline')
        [day1_track3.append(talk) for talk in talks_day1_track3]
        
        day1_track4 = soup.find('div', id='tab-lv21-third').find('div', class_='timeline')
        [day1_track4.append(talk) for talk in talks_day1_track4]

        day2_track1 = soup.find('div', id='tab-lv22-first').find('div', class_='timeline')
        [day2_track1.append(talk) for talk in talks_day2_track1]
        
        day2_track2 = soup.find('div', id='tab-lv22-second').find('div', class_='timeline')
        [day2_track2.append(talk) for talk in talks_day2_track2]
        
        day2_track3 = soup.find('div', id='tab-lv22-third').find('div', class_='timeline')
        [day2_track3.append(talk) for talk in talks_day2_track3]
        
        day2_track4 = soup.find('div', id='tab-lv22-third').find('div', class_='timeline')
        [day2_track4.append(talk) for talk in talks_day2_track4]

    
        
