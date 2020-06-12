from multiprocessing import Process
import time
import threading
import json
from datetime import datetime
import random
#import tkinter as tk


stats = [0, 100] # placeholder, money, idk
print(stats[1])
upgrades = [0, 0] # placeholder, workers

cash = 100

now = datetime.now()

    
def c():
    print('Started. hopefully running all good xD')

   # while True:
        #time.sleep(1)
        #cash = cash + 1

def moneyLoop():
    while True:
        time.sleep(1)
        add = 1
        for _ in range(upgrades[1]):
            add = add + 1
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

if __name__ == '__main__':
    print('starting main functions')
    time.sleep(1)
    thread = threading.Thread(target=moneyLoop)
    thread.start()
    while True:
        a = input()
        args = getArguments(a)
        if a == 'exit':
            exit()
        elif a == 'money':
            print(stats[1]) 
        elif a == 'upgrade worker':
            if stats[1] >= 100:
                stats[1] = stats[1] - 100
                upgrades[1] = upgrades[1] + 1
                print('purchased worker')
            else:
                print('not enough money')
        elif a == 'debug':
            print(upgrades[1])
            add = 1
            for _ in range(upgrades[1]):
                add = add + 1
            print(add)
        elif a == 'save':
            print('saving..')
            File = open('save.txt', 'w')
            File.write(str(stats[1]) + '\n_\n' + str(upgrades[1]))
            File.close()
            print('saved')
        elif a == 'load':
            try:
                print('loading..')
                File = open('save.txt', 'r')
                data = File.readlines()
                stats[1] = int(data[0])
                upgrades[1] = int(data[2])
                File.close()
                print('loaded')
            except:
                print('woops something went wrong, please report this bug to the creator.')
                File = open('latest_error.txt', 'w')
                File.write('load error ' + now.strftime("%Y %D %H:%M:%S"))
                File.close()
                print('error log saved.')
        elif args[0] == 'argtest':
            try:
                print(args[1])
            except:
                print('woops something went wrong, please report this bug to the creator.')

            
