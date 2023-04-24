import requests
import json

from config import API_URL
from objects.Stamp import Stamp

# スタンプ情報を取得
def get_stamp(ses: requests.Session, stampId: str) -> Stamp:
    raw = ses.get(API_URL + "/stamps/" + stampId)
    dec = raw.content.decode("utf-8")
    obj = json.loads(dec)
    return Stamp(**obj)