import os

message = 'The directory already exists.'
testdir = 'testdir'

try :
    home = os.path.expanduser("~")
    print(home)

    if not os.path.exists(os.path.join(home,testdir)):
        os.makedirs(os.path.join(home,testdir))
    else:
        print(message)
except Exception as e:
    print(e)