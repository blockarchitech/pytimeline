import requests
import json

def pushPin(title, body, subtitle, time, token):
    # valid times are:
    # 1 - Instant
    # 2 - In 30 min. (Timeline Subscription)
    # 3 - In 60 min. 
    # 4. - In 3 hours (Free)
    pin = {
    "time":f"{time}",
    "layout":{
        "type": "genericPin",
        "title": f"{title}",
        "body": f"{body}",
        "subtitle": f"{subtitle}",
        "tinyIcon": "system://images/NOTIFICATION_GENERIC"},
        "token": f"{token}"
    }
    pinjson = json.dumps(pin)
    r = requests.post('https://willow.systems/pinproxy-ifttt/', data=pinjson)
    if r.status_code == 200:
        return 200
    else:
        return f"{r.status_code} {r.text}"
