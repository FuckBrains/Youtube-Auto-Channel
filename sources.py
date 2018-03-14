import random
import time
import json

_universal_tags = ['epic', 'funny', 'dank', 'meme', 'dankness', 'win', 'fail', 'laugh', 'lose', 'hot', 'boobs', 'girl', 'dog', 'cat', 'gaming', 'nerd', 'awesome', 'cool']

_content_sources = [
    {
        'subreddit': 'gifs',
        'titles': ['Greatest Gifs of All Time'],
        'tags': _universal_tags + ['gif'],
        'text': True
    },
    {
        'subreddit': 'dankmemes',
        'titles': ['DANKEST MEMES'],
        'tags': _universal_tags + ['spongebob', 'vine'],
        'text': False
    },
    {
        'subreddit': 'anime_irl',
        'titles': ['BEST ANIME MEMES'],
        'tags': _universal_tags + ['kawaii', 'anime', 'baka', 'neko', 'lewd', 'nippon', 'japan'],
        'text': False
    },
    {
        'subreddit': 'woahdude',
        'titles': ['INSANE VIDEO, DO NOT WATCH!!!'],
        'tags': _universal_tags + ['trippy', 'insane', 'crazy'],
        'text': True
    },
    {
        'subreddit': 'funny',
        'titles': ['If you laugh you MUST like this video!'],
        'tags': _universal_tags + ['halarious', 'lol', 'lmao'],
        'text': True
    },
    {
        'subreddit': 'wtf',
        'titles': ['WTF DID I JUST WATCH!!!!!'],
        'tags': _universal_tags + ['wtf', 'disturbing', 'crazy', 'why', 'omg'],
        'text': True
    },
    {
        'subreddit': 'aww',
        'titles': ['This is so cute OMG!'],
        'tags': _universal_tags + ['cute', 'adorable', 'bunny', 'rabbit', 'cat', 'kitten', 'dog', 'puppy'],
        'text': False
    },
    {
        'subreddit': 'interestingasfuck',
        'titles': ['THE CRAZIEST SHIT YOU WILL SEE TODAY'],
        'tags': _universal_tags + ['trippy', 'insane', 'crazy'],
        'text': True
    },
    {
        'subreddit': 'oddlysatisfying',
        'titles': ['This is the Most Satisfying Video'],
        'tags': _universal_tags + ['crazy', 'satisfying', 'oddly', 'nice'],
        'text': False
    },
    {
        'subreddit': 'gentlemanboners',
        'titles': ['The sexiest girls EVER'],
        'tags': _universal_tags + ['attractive', 'cute', 'sexy', 'sex', 'boner', 'tits', 'dress', 'woman'],
        'text': False
    },
    {
        'subreddit': 'gaming',
        'titles': ['Greatest Gaming Memes'],
        'tags': _universal_tags + ['gamergirl', 'overwatch', 'tf2', 'moba', 'league', 'legends', 'gamer', 'fallout'],
        'text': True
    },
    {
        'subreddit': 'wholesomememes',
        'titles': ['Worlds most wholesome memes'],
        'tags': _universal_tags + ['happy', 'wholesome', 'heart', 'warming'],
        'text': False
    },
    {
        'subreddit': 'mildlyinteresting',
        'titles': ['OMG!!'],
        'tags': _universal_tags + ['insane', 'crazy', 'interesting', 'cool'],
        'text': True
    },
    {
        'subreddit': 'BetterEveryLoop',
        'titles': ['Greatest Gifs of All Time'],
        'tags': _universal_tags + ['insane', 'crazy', 'interesting', 'cool', 'gif', 'video'],
        'text': True
    }
]


#a class that represents a source subreddit with a title, tags and boolean of whether or not text should be used in the video for this source
class _source():
    def __init__(self, subreddit, title, tags, text):
        self.subreddit = subreddit
        self.title = title
        self.tags = tags
        self.text = text

#gets all the latest titles from the list of titles
def _get_titles():
    with open('used_titles.txt', 'r') as f:
        all_titles = json.loads(f.read())
    return all_titles
    
#finds out how many other videos with the same title have been made and slaps the correct number on the end
#ie, "You laugh you lose" becomes "You laugh you lose #645"
def _next_title(title):
    all_titles = _get_titles()
    if title in all_titles:
        title = title + ' #' + str(all_titles[title] + 1)
    else:
        title = title + ' #1'
    return title

#updates the list of used titles with title
#this should only be called AFTER video has been successfully uploaded
def update_titles(title):
    title, num = title.split(' #')
    num = int(num)
    all_titles = _get_titles()
    all_titles[title] = num
    with open('used_titles.txt', 'w') as f:
        f.write(json.dumps(all_titles))

#gets a source to download content from
def _get_source(index):
    src = _content_sources[index]
    title = _next_title(random.choice(src['titles']))
    return _source(src['subreddit'], title, src['tags'], src['text'])

#returns a list of an entire day of scheduled videos
def full_day_sources():
    return [_get_source(i) for i in range(len(_content_sources))]
