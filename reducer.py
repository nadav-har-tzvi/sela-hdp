#!/usr/bin/python

import sys

current_user = None
current_cnt = 0

for line in sys.stdin:
    line = line.strip()
    user, cnt = line.split('\t')

    if user == current_user:
        current_cnt += int(cnt)
    else:
        interim_result = '{}\t{}'.format(current_user, current_cnt)
        print(interim_result)
        current_user = user
        current_cnt = int(cnt)

print('{}\t{}'.format(current_user, current_cnt))
