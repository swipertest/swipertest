'''
第三方配置
'''



#互亿无线短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account':'C01525302',
    'password':'56f1d3d1d5e954c6ce8479406c9c1337',
    'content':"您的验证码是：%s,请不要把验证码泄露给其他人。",
    'mobile':None,
    'format':'json',
}
