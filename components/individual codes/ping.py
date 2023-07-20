# This is a ping command file
import os
import sys
#os.system('cls')
def ping(ip):
    print('-'*60)
    try:
        # if it is not != 0 then something is wrong and raise Exception
        # also only run 4 packets and exit.
        if os.system('ping -c 4 {}'.format(ip)) != 0: 
            raise Exception('IP does not exist')
    except:
        print('Command does not work')
    print('-'*60)
    sys.exit(1)

