#!/usr/bin/python

# Important: Use python3 or higher to run this program!

# Author: @m4gu5
# License: GPL

import os
import sys
from random import randrange

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def read(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def versionCheck():
    if sys.version_info[0] < 3:
        sys.stdout.write("You need python3 or higher to run this program.\n")
        exit(1)

def printBanner():
    print(' KKKKKKKKK0 \'000.    d00    ,d0XXKOl.   k00;      \'00k  .KKKKK0Od;   ')
    print('.MMMdccccc: ;MMM\'    OMM. .KMMO::oWMW;  XMM:      ;MMX  \'MMMc;cxWMN: ')
    print('.MMM:.....  ;MMM\'    OMM. 0MMK    :Okd  XMM:      ;MMX  \'MMM.   ,MMM\'')
    print('.MMMMMMMMd  ;MMM\'    OMM..MMMx          XMM:      ;MMX  \'MMM.    NMMc')
    print('.MMM;....   ;MMM,    0MM  KMM0    .olc  XMM:      ;MMX  \'MMM.   ;MMM\'')
    print('.MMMdccccc: .XMMKc;;oMMO  .XMMk:;lNMWc  XMMOlllll ;MMX  \'MMMlclkWMN; ')
    print(' KKKKKKKKK0   ckKXNXKx;     ;xKXNXOl.   kKKKKKKKK.,KKk  .KKKKK0Od,   ')

def showMenu():
    print('-----------')
    print('EUCLID Menu')
    print('-----------')
    print('[0] Show Pi')
    print('[1] Input digits one by one')
    print('[2] Value at position')
    print('[3] Input all at once')
    print('[x] Exit')

def printPi():
    numberOfDigits = input('Number of digits to show: ')
    try:
        numberOfDigits = int(numberOfDigits)
    except:
        numberOfDigits = 100
    if numberOfDigits > len(decimalPlaces):
        numberOfDigits = len(decimalPlaces)
    groupDigits = input('Group digits? (y/n) ').lower()
    if groupDigits == '':
        groupDigits = 'y'
    if groupDigits == 'y':
        groupSize = input('Group size: ')
        try:
            groupSize = int(groupSize)
        except:
            groupSize = 5
    groupedPi = ''
    for i in range(0, numberOfDigits):
        if groupDigits == 'y' and i > 0 and i % groupSize == 0:
            groupedPi += ' '
        groupedPi += decimalPlaces[i]
    print('3.' + groupedPi)

def getNumberCount():
    while True:
        choice = input('How many decimals? ')
        try:
            choice = int(choice)
            return choice
        except:
            pass

def inputOneByOne():
    numberCount = getNumberCount()

    failed = False   
 
    for i in range(1, numberCount + 1):
        sys.stdout.write('(' + str(i) + ') ')
        sys.stdout.flush()
        number = getch.read()[0]
        sys.stdout.write(number + '\n')

        if number != decimalPlaces[i - 1]:
            print('You failed at decimal ' + str(i))
            print('Next digit would have been ' + decimalPlaces[i - 1])
            failed = True
            break
    if not failed:
        print('\o/ You made it! \o/')

def valueAtPosition():
    numberCount = getNumberCount()
    
    while True:
        position = randrange(numberCount)
        inp = input('(' + str(position + 1) + ') ')
    
        if inp != decimalPlaces[position]:
            print('Digit at position ' + str(position + 1) + ' is ' + decimalPlaces[position]) 
            break

def inputAllAtOnce():
    piInput = input('3.')
   
    failed = False 
    for i in range(0, len(piInput)):
        if piInput[i] != decimalPlaces[i]:
            failed = True
            print('You managed to remember ' + str(i + 1) + ' decimals')
            break
    if not failed:
        print('You got all ' + str(i + 1) + ' digits right!')


def promptThenClearConsole():
    print('----------------------------')
    print('Press any key to continue...')
    getch.read()
    os.system('cls' if os.name == 'nt' else 'clear')

# First 1000 decimals
decimalPlaces = '14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893'

versionCheck()

getch = _Getch()

print()
printBanner()
print()

while 1:
    showMenu()
    choice = input('Choice: ')

    try:
        choice = int(choice)
    except:
        break

    if choice == 0:
        printPi()
    elif choice == 1:
        inputOneByOne()
    elif choice == 2:
        valueAtPosition()
    elif choice == 3:
        inputAllAtOnce()
    else:
        break
    promptThenClearConsole()