import time
import hashlib
from urllib.request import urlopen, Request
from playsound import playsound

url = Request("https://biggeek.ru/catalog/apple-airpods",
              headers={"User-Agent": "Mozilla/5.0"})

response = urlopen(url).read()


currentHash = hashlib.sha224(response).hexdigest()
print("running")
while True:
    try:
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(20)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if newHash == currentHash:
            continue
        else:
            for _ in range(5):
                playsound('/home/igor/Downloads/budilnik.mp3')
            print("something changed")
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    except Exception as e:
        print("error")
