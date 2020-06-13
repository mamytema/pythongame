from multiprocessing import Process
import time
import threading
from datetime import datetime
import random
import math
import string

history = ['game started']

stats = [0, 100] # placeholder, money, idk
upgrades = [0, 0, 0, 0, 0] # placeholder, workers

cash = 100

now = datetime.now()

version = 'v.0.0.3-indev'


def income():
    add = 1
    for _ in range(upgrades[1]):
        add = add + 1
    for _ in range(upgrades[2]):
        add = add + 2
    for _ in range(upgrades[3]):
        add = add + 5
    return add

def moneyLoop():
    while True:
        time.sleep(1)
        add = income()
        stats[1] = stats[1] + add
        
def getArguments(str):
    args = []
    storedstr = ''
    for s in str:
        if s == ' ':
            args.insert(len(args) + 1,storedstr)
            storedstr = ''
        else:
            storedstr = storedstr + s
    args.insert(len(args) + 1,storedstr)
    return args
def _upgrade(num = 1, cnum = 1, price = 100, multi = 1.25):
    # defining
    upgradenum = num
    currencynum = cnum

    upgradenum = 1
    currencynum = 1
    for i in range(upgrades[upgradenum]):
        price = price * multi
    price = math.floor(price)
    print('purchasing..')
    if stats[currencynum] >= price:
        stats[currencynum] - price
        upgrades[upgradenum] = upgrades[upgradenum] + 1
        print('purchased!')
    else:
        print('you dont have enough money!\nmoney required: '+str(price))


def upgrade(args):
    try:
        if args[1] == 'worker':
            _upgrade(1, 1, 100, 1.25)
        elif args[1] == 'superworker' or args[1] == 'super' and args[2] == 'worker':
            _upgrade(2, 1, 250, 1.50)
        elif args[1] == 'manager':
            _upgrade(3,1,500,1.5)
        else:
            print('you did not specify anything/ invalid id.')
    except:
        print('console>upgrade>function error\nDid you specify an argument?')

def save():
    _data = []
    for v in stats:
        _data.insert(len(_data) + 1, str(v) + '*')
    for v in upgrades:
        _data.insert(len(_data) + 1, str(v) + '*')
    _file = open('save.txt', 'w')
    r_data = ''
    for v in _data:
        r_data = r_data + v
    _file.write(r_data)
    _file.close()


def filterData(_s):
    nums = [1,2,3,4,5,6,7,8,9]
    i = 0
    for v in nums:
        nums[i] = str(nums[i])
        i = i + 1
    _ns = ''
    for v in _s:
        for z in nums:
            if v == z:
                _ns = _ns + v
    print(_ns)
    return _ns



def load():
    #try:
        # getting the data
        _file = open('save.txt', 'r')
        data = _file.readlines()
        _file.close()
        # reading the data
        _data = []
        _storage = ''    
        nums = ['1','2','3','4','5','6','7','8','9','0' ]
        i = 0
        for v in data:
            for z in range(len(v)):
                _skip = False
                if v[z] == '*':
                    _data.insert(len(_data)+1, _storage)
                    _storage = ''
                    _skip = True
                    i = i + 1
                if _skip == False:
                    for n in nums:
                        if n == v[z]:
                            _storage = _storage + v[z] 
    
        statlines = [
            0,
            1
        ]
        upgradelines = [
            0,
            2,
            3,
            4,
            5
        ]
        i = 0
        for v in statlines:
            stats[i] = int(_data[v])
            i = i + 1
        i = 0
        for v in upgradelines:
            upgrades[i] = int(_data[v])
            i = i + 1
        history.insert(len(history)+1, 'loaded file.')
            
    #except:
        #print('error something went wrong. did you save the file previously, was the file edited?')
        #history.insert('loading error.')

if __name__ == '__main__':
    print('starting main functions..')
    time.sleep(1)
    thread = threading.Thread(target=moneyLoop)
    thread.start()
    print('started!')
    print('-----------------------------\nWelcome to Idle Python Game'+ version + '\nThis is a test game for now.\nRead README for faq, type help for commands.\n-----------------------------')
    while True:
        a = input('>')
        a = a.lower()
        args = getArguments(a)
        if a == 'exit':
            exit()
        elif a == 'money':
            print(stats[1]) 
        elif args[0] == 'upgrade':
            upgrade(args)
        elif a == 'debug':
            print(upgrades[1])
            add = 1
            for _ in range(upgrades[1]):
                add = add + 1
            print(add)
        elif a == 'save':
            print('saving..')
            save()
            print('saved')
        elif a == 'load':
            try:
                print('loading..')
                load()
                print('loaded')
            except:
                print('An error occured. Was the "save.txt" file changed recently?')
        elif args[0] == 'argtest':
            try:
                print(args[1])
            except:
                print('woops something went wrong, please report this bug to the creator.')
        elif args[0] == 'help':
            h = [
                'help - you are in this menu',
                'save - saves the game',
                'load - loads the game',
                'upgrade - purchases a specific upgrade',
                'upgrades - shows all upgrades',
                'money - shows your money',
                '.debug ? - .debug help menu'
            ]
            print('Help menu')
            for v in h:
                print(v)
        elif args[0] == 'upgrades':
            u = [
                'worker - increases income by 1',
                'super worker - increases income by 2',
                'manager - increases income by 5',
            ]
            print('Upgrades\n use "upgrade <upgrade>" to use upgrade!')
            for v in u:
                print(v)
        elif args[0] == '.debug':
            try:
                if args[1] == 'all':
                    print('Your income/s:')
                    print(income())
                    print('Your balance:')
                    print(stats[1])
                    print('All of your upgrades (sorted):')
                    for v in upgrades:
                        print(v)
                elif args[1] == 'income':
                    print('Your income/s:')
                    print(income())
                elif args[1] == 'bal':
                    print('Your balance:')
                    print(stats[1])
                elif args[1] == 'upgrades':
                    print('All of your upgrades (sorted):')
                    for v in upgrades:
                        print(v)
                else:
                    coms = [
                        'all - outputs everything',
                        '? (or blank) - debug help',
                        'income - outputs your income',
                        'bal - outputs your balance',
                        'upgrades - outputs your upgrades'
                    ]
                    for v in coms:
                        print(v)
            except:
                print('something went wrong, did you pass an argument?')
                

            
