import random

def shorten(url):
    short_url = '127.0.0.1:8000/'+str(random.randint(1,100000))
    return short_url