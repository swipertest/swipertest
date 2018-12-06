import random

import requests

from swiper import config

def gen_verify_code(length=6):
    # 产生一个验证码
    verify_code = random.randrange(10**(length-1),10**(length))
    return verify_code

def send_sms(phonenum,message):
    v_code=gen_verify_code()
    sms_cfg = config.HY_SMS_PARAMS.copy()
    config.HY_SMS_PARAMS['content'] = config.HY_SMS_PARAMS['content']%v_code
    config.HY_SMS_PARAMS['mobile'] = phonenum
    requests.post(config.HY_SMS_PARAMS,data=config.HY_SMS_PARAMS)