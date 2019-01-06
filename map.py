#!/usr/bin/python

import csv
import sys

reader = csv.reader(sys.stdin)

def count_posts_by_user():
    posts_by_user = {}
    for reddit_post in reader:
        if len(reddit_post) > 0:
            try:
                posts_by_user.setdefault(reddit_post[15], 0)
                posts_by_user[reddit_post[15]] += 1
            except IndexError:
                continue
    for user, cnt in posts_by_user.items():
        print('{user}\t{cnt}'.format(user=user, cnt=cnt))


count_posts_by_user()
