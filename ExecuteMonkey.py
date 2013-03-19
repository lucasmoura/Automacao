# -*- coding: cp1252 -*-

import subprocess
import os.path
import os
import sys

# --------------------------- #
#                             #
#    Variaveis para Edicao    #
#                             #
# --------------------------- #

#Pasta do Android SDK
ANDROID_HOME = 'C:/Users/Matheus/AppData/Local/Android/android-sdk'

#Pasta onde esta a pasta "com" da bilbioteca Android View CLient
VIEW_CLIENT = r'D:\programacao\Python\PyDevWorkspace\ViewClient-Modified'

#Arquivo dos Testes MonkeyRunner
testFile = r"D:\programacao\Python\PyDevWorkspace\ExecuteMonkeyRunner\main.py"


# ------------------------------ #
#                                #
#    Constantes Nao Editaveis    #
#                                #
# ------------------------------ #

MY_PATH_LIST = [
ANDROID_HOME,
os.path.join(ANDROID_HOME, 'tools'),
os.path.join(ANDROID_HOME, 'platform-tools')]


if not os.path.isdir(ANDROID_HOME):
    print 'O diretorio ' + ANDROID_HOME + ' nao existe.'
    raw_input("Pressione ENTER...")
    sys.exit(0)

if not os.path.isdir(VIEW_CLIENT):
    print 'O diretorio ' + VIEW_CLIENT + ' nao existe.'
    raw_input("Pressione ENTER...")
    sys.exit(0)
    
if not os.path.isdir(os.path.join(VIEW_CLIENT, 'com')):
    print 'O diretorio "com" nao esta no caminho do View Client informado.'
    raw_input("Pressione ENTER...")
    sys.exit(0)

if not os.path.isfile(testFile):
    print 'O arquivo de testes nao existe. O arquivo passado foi' + testFile
    raw_input("Pressione ENTER...")
    sys.exit(0)

for i in MY_PATH_LIST:
    if not os.path.isdir(i):
        print 'O diretorio ' + i + ' nao existe. Cheque a instalacao do Android.' 
        raw_input("Pressione ENTER...")
        sys.exit(0)  

bar_type = '/' if sys.platform != 'win32' else '\\'

if os.getenv('ANDROID_HOME') != ANDROID_HOME.replace('/', bar_type):
    os.putenv('ANDROID_HOME', ANDROID_HOME)
    
if os.getenv('VIEW_CLIENT') != VIEW_CLIENT.replace('/', bar_type):
    os.putenv('VIEW_CLIENT', VIEW_CLIENT)
    
separator = ':' if sys.platform != 'win32' else ';'

path = os.getenv('PATH')
for i in MY_PATH_LIST:
    if i.replace('/', bar_type) not in path:
        path = path + separator + i.replace('/', bar_type)
os.putenv('PATH', path)

#Start
subprocess.call(u'monkeyrunner  ' + testFile , 
                stdin=None, stdout=None, stderr=None, shell = True)

if sys.platform != 'win32':
    sys.exit(0)
raw_input("Pressione ENTER...")