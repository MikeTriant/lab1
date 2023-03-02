import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

userurl = input("url:")
url = userurl  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    text1 = response.headers
    print(text1,"\n")
    text2 = response.cookies
    if len(text2)>0:
        print("Website cookies:")
        for item in text2:
            exp = datetime.datetime.fromtimestamp(item.expires)
            print("Cookie name:", item.name,", Expires:", exp)
    else:
        print("There are no cookies.")