import os
import sys
#Command for Window user
def tracert(route_to_test):
    print('-'*60)
    try:
        if os.system('tracert {}'.format(route_to_test)) != 0: # if it is not != 0 then something is wrong and raise Exception
            raise Exception('Route does not exist')
    except:
        print('Command does not work')
    print('-'*60)
    sys.exit(1)

#Command for Mac user
def traceroute(route_to_test):
    print('-'*60)
    try:
        if os.system('traceroute {}'.format(route_to_test)) != 0: # if it is not != 0 then something is wrong and raise Exception
            raise Exception('Route does not exist')
    except:
        print('Command does not work')
    print('-'*60)
    sys.exit(1)


