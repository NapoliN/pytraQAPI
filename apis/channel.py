import json
import requests
import datetime
from config import API_URL

# チャンネル一覧の取得
def get_all_channels(ses:requests.Session):
    r = ses.get(API_URL + "/channels")
    return json(r.content.decode(encoding="utf-8"))

# チャンネルからメッセージを取得
def get_messages(ses:requests.Session,channelId:str):
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    js = {
        "limit" : 50,
        "since" : datetime.datetime(2023,3,1,tzinfo=JST).isoformat(),
        "until" : datetime.datetime(2023,4,1,tzinfo=JST).isoformat()
    }
    r = ses.get(API_URL + "/channels/" + channelId + "/messages",json=js)
    return r.content.decode("utf-8")

# チャンネル情報の取得
def get_channel(ses:requests.Session, channelID:str):
    r = ses.get(API_URL + "/" + channelID)
    return r.content.decode("utf-8")