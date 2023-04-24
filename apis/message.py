import requests
import datetime
import json
import tqdm
from time import sleep
from math import ceil
from typing import List

from config import API_URL
from objects.Message import Message

def __get_messages(ses: requests.Session, since: datetime.datetime, until: datetime.datetime):
    # アクセス件数の取得
    js = {
            "after": since.isoformat(),
            "before" : until.isoformat(),
            "limit" : 1
        }
    raw = ses.get(API_URL + "/messages",json=js)
    dec = raw.content.decode("utf-8")
    totalHits = json.loads(dec)["totalHits"]
    print("Hits: ",totalHits)
    print("Getting messages")
    # 指定日のログを全件取得
    messages = []
    for i in tqdm.tqdm(range(ceil(totalHits/100))):
        js = {
            "after": since.isoformat(),
            "before" : until.isoformat(),
            "offset" : i * 100,
            "limit" : 100
        }
        raw = ses.get(API_URL + "/messages",json=js)
        dec = raw.content.decode("utf-8")
        messages_json = json.loads(dec)["hits"]
        messages.extend(messages_json)
        sleep(0.1)
    return messages

# 日時を指定してメッセージを取得
def get_messages(ses: requests.Session, since: datetime.datetime, until: datetime.datetime) -> List[Message] :
    lst = __get_messages(ses,since,until)
    return [Message(**o) for o in lst]
