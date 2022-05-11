import re, requests

for i in range(1, 21):
    r = requests.get(f'https://www.rolimons.com/leaderboard/{i}').text
    usernames = re.findall('py-1 text-truncate" title="(.*?)"', r)
    with open('leaderboard.txt', 'a') as f:
        f.writelines([u+'\n' for u in usernames])

input('Done.')