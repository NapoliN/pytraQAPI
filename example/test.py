from typing import TypeVar, Generic
from collections import defaultdict
import datetime
from apis.authentication import login
from apis.message import get_messages
from apis.stamp import get_stamp
from objects.Stamp import Stamp
from time import sleep

from os import environ

from tqdm import tqdm


T = TypeVar("T")

class Map(Generic[T]):
    def __init__(self) -> None:
        self.dict = dict()

    def set(self,key:str,item:T) -> None:
        self.dict[key] = item

    def hasKey(self,key) -> bool:
        return key in self.dict

    def get(self,key:str) -> Stamp:
        if(not self.hasKey(key)):
            raise ValueError()
        return self.dict[key]

with login(environ["TRAQ_USERNAME"], environ["TRAQ_PASSWORD"]) as ses:
    stamp_map = Map[Stamp]()
    stamp_count = defaultdict(int)
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    since = datetime.datetime(2023,4,23,23,tzinfo=JST)
    until = datetime.datetime(2023,4,24,0,tzinfo=JST)
    messages = get_messages(ses,since,until)

    for mes in tqdm(messages):
        for stmp in tqdm(mes.stamps,leave=False):
            id = stmp.stampId
            if(not stamp_map.hasKey(id)):
                stamp_map.set(id, get_stamp(ses,id))
                sleep(0.1)
            stamp_count[id] += 1

    sorted_stamp_count = sorted(stamp_count.items(),key=lambda x: x[1],reverse=True)
    f = open("usage.txt","w")
    for i, (key, value) in enumerate(sorted_stamp_count):
        stmp = stamp_map.get(key)
        f.write(f"|{i}|:{stmp.name}: `{stmp.name}` | {value}|\n")
            