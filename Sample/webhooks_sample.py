from pathlib import Path
import requests
import json

"""
var webhookUrl = "https://maker.ifttt.com/trigger/"+iftttEventName+"/with/key/"+key
"""

EVENT_FILE = "Webhook/event_key.json"

# IFTTT_Webhook
def ifttt_webhook(eventid, keycode):

    payload = {"value1": "Fujinaga", "value2": "Seiji", "value3": "test" }
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + keycode
    response = requests.post(url, data=payload)

# ここからスタート
if __name__ == '__main__':
    print ("IFTTT連携開始")

    # IFTTT_Webhook
    path = Path(EVENT_FILE)
    if path.exists():
        event = json.loads(path.read_text())
        eventid = event.get("event_id")
        keycode = event.get("key_code")

    ifttt_webhook(eventid, keycode)

    print ("IFTTT連携終了")
 


