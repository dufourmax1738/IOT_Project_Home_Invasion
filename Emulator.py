import random

import requests


def postSound():
    URL = "http://127.0.0.1:5000/sensors/10/sound"



    data = {"sound":random.randint(20,100)}

    r = requests.post(url=URL, data = data, headers={'Content-Type': 'application/json'})

    finalData = r.json()
    print(finalData)

def postMotion():
    URL = "http://127.0.0.1:5000/sensors/15/motion"

    data = {"motion": random.randint(0, 1)}

    r = requests.post(url=URL, data=data, headers={'Content-Type': 'application/json'})

    finalData = r.json()
    print(finalData)