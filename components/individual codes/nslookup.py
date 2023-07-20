import os
import sys

def nslookup(Host_name):
    print('-'*70)
    try:
        if os.system('nslookup {}'.format(Host_name)) != 0: # if it is not != 0 then something is wrong and raise Exception
            raise Exception('Host does not exist')
    except:
        print('Command does not work')
    print('-'*70)
    sys.exit(1)

