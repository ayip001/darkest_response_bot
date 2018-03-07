#!./ENV/bin/python
import praw
import os

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("darkest_response_bot")
# subreddit = reddit.subreddit("darkestdungeon")
comments = subreddit.comments(limit=25)
newest_comment = subreddit.comments(limit=1)

def parse_comment(comment):
    print (comment.id)
    print (comment.body)
    print ("Contains 5: " + str("5" in comment.body))
    if "5" in comment.body:
        comment.reply("ayy lmao xdxdxd")

def set_parse_until(post_id):
    with open("parse_until.txt", "w") as f:
        f.write(post_id)

def get_parse_until():
    if not os.path.isfile("parse_until.txt"):
        return ""
    else:
        with open("parse_until.txt", "r") as f:
           return f.read()
 
def test_scan():
    """
    Iterates through newest comments until it reachest the most recently
    parsed comment last time, saved in a .txt file
    """
    for comment in comments:
        if comment.id == parse_until:
            return
        parse_comment(comment)

if __name__ == '__main__':
    """
    Retrive the most recently parsed comment, then overwrite it
    TODO: FIX THE WAY I GET THE NEWEST COMMENT ID
    """
    parse_until = get_parse_until()
    print ("parse until " + parse_until);
    for comment in newest_comment:
        set_parse_until(comment.id)
    """
    Iterate through comments
    """
    test_scan()
