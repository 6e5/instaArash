import requests, os, sys, ast

###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
    W = "\033[0m"
    G = "\033[32;1m"
    R = "\033[31;1m"
else:
    W = ''
    G = ''
    R = ''
###################################################################
print (R + '_     _'.center(44))
print ("o' \.=./ `o".center(44))
print ('(o o)'.center(44))
print ('ooO--(_)--Ooo'.center(44))
print (W + ' ')
print ('A L - K I N G'.center(44))
print ('> A R A S H'.center(44))
print (' ')
def menu_bot():
    print ('''
   Number                  INFO
 ---------   ------------------------------------
   [ 01 ]      Instagram Views
   [ 02 ]      Instagram Followers
   [ 03 ]      Instagram Likes
   [ 04 ]      Instagram Comments
   [ 05 ]      Instagram Post Saves
   [ 06 ]      Instagram Story Viewers
   [ 00 ]      Exit
''')
    y = input('3Rash: ' )
    if y == '1':
        start()
    elif y == '01':
        start()
    elif y == '0':
        sys.exit()
    elif y == '00':
        sys.exit()
    else:
        sys.exit()

def start():
    postUrl = input('[+] Post URL: ')
    code = postUrl
    print(code)
    def run(code):
        newCode = code
        print('[+] Getting Media ID...')
        r = requests.get('https://igpro.me/robotControl')
        r = requests.get('https://igpro.me/ajax/getPostInformation?media='+newCode)
        info = r.text
        x = ast.literal_eval(info)
        pID = x['media_code']
        data = {'media_code': pID, 'count': '3000', 'required':'10000' }
        print('[+] Starting Server 01')
        r = requests.get('https://igsub.me/robotControl')
        print('[+] Home Page - Start')
        r = requests.get('https://igsub.me')
        print('[+] Loading...')
        r = requests.get('https://igsub.me/postViews')
        print('[+] Process Started.')
        r = requests.post('https://igsub.me/posts/postViews', data = data)
        print('[+] Please wait...')
        if 'completed' in r.text:
            print('[+] Completed.')
            print('[+] Server 02 START...')
        else:
              print('[-] Failed - Trying Second Server')
        print('[+] Starting Server 02')
        r = requests.get('https://igpro.me/robotControl')
        print('[+] Home Page - Start')
        r = requests.get('https://igpro.me')
        print('[+] Loading...')
        r = requests.get('https://igpro.me/postViews')
        print('[+] Process Started.')
        r = requests.post('https://igpro.me/posts/postViews', data = data)
        print('[+] Please wait...')
        response=r.text
        if 'completed' in r.text:
            print('[+] Completed.')
            print('[+] Going Again :)')
            run(newCode)
        else:
              print('[-] Failed - Script will restart.')
              run(newCode)
    run(code)

menu_bot()
