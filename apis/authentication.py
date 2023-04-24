import requests
from http import HTTPStatus
from config import API_URL

def login(id,password):
    ses = requests.session()
    r = ses.post(API_URL + "/login",json={"name":id, "password":password})
    
    if(r.status_code != HTTPStatus.NO_CONTENT):
        raise ValueError()
    print(ses.cookies)
    return ses