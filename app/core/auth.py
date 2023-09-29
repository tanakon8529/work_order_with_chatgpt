import jwt
from fastapi import APIRouter, HTTPException, Header
from loguru import logger
from datetime import datetime

from app.settings.configs import FIRST_DEVUSER, FIRST_DEVUSER_PASSWORD, JWT_PUBLIC_KEY, \
                                ACCESSTOKEN_FILE_PATH
from app.core.base_model import UserInfo                    
from app.utils.json_util import json_controls

js_controls = json_controls()
router = APIRouter()

def decode_token_userinfo(token: str):
    try:
        payload = jwt.decode(token, JWT_PUBLIC_KEY, algorithms="HS256")
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="secret key invalid : {}".format(e))

def verify_grant_type(type: str):
    try:
        if type == "client_credentials":
            return type
        elif type == "get_client_credentials":
            return type
        else:
            raise HTTPException(status_code=401, detail="Type invalid(01)")
    except Exception as e:
        logger.error(f"{e}")
        raise HTTPException(status_code=401, detail="Type invalid(01) {}".format(e))

def check_expire_access_token(token):
    time_now = datetime.now()
    token_file = js_controls.read_json_file(ACCESSTOKEN_FILE_PATH)
    status_token = None

    if token_file["access_token"] == token:
        date_time_obj = datetime.strptime(token_file["time_stamp"], '%Y-%m-%d %H:%M:%S')
        try:
            logger.debug(f"stamp_time : {date_time_obj} : {time_now}")
            status_token = True
            if date_time_obj < time_now:
                status_token = False
                logger.debug("access_token expired !!!")
        
        except Exception as e:
            logger.error(f"{e}")
            raise HTTPException(status_code=401, detail="access_token invalid : {}".format(e))

    return status_token


def verify_token_user_info(auth: str = Header(...)):
    status_token = check_expire_access_token(auth)
    if status_token == True:
        return status_token
    elif status_token == False:
        raise HTTPException(status_code=401, detail="access_token expired")
    else:
        raise HTTPException(status_code=401, detail="auth invalid(01)")
