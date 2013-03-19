# -*- coding: cp1252 -*-

# --------------------------- #
#                             #
#    Cabecalho Obrigatorio    #
#                             #
# --------------------------- #
import sys
import os
import time

#import da Biblioteca
sys.path.append(os.getenv('VIEW_CLIENT'))
from viewclient import ViewClient
#import do MonkeyRunner
from com.android.monkeyrunner import MonkeyRunner


# --------------------------- #
#                             #
#      Comeco do Script       #
#                             #
# --------------------------- #

def ct58(device, vc):
    '''
    Test Item: ANDROID OS Version 
    Action: Check the operating system version
    Expected Result: Android version must be 3.x or higher
    '''    
    release = device.getProperty('build.version.release')
    
    if int(release[0]) >= 3:
        return ('\033[32m'+'Passou'+'\033[0;0m', release)
    else:
        return ('\033[31m'+'Nao Passou'+'\033[0;0m', release)


def ct155(device, vc):
	'''
	Test Item: SW BUTTON Home Button
	Action: Use the Home button and check if it is working
	Expected Result: Home button is working
	'''
	
	resultado_esperado = device.takeSnapshot()
	
  	device.press("KEYCODE_CALENDAR", "DOWN_AND_UP") 
  	time.sleep(2)
  	
  	device.press("KEYCODE_HOME", "DOWN_AND_UP")
	time.sleep(2)
	
	resultado_obtido = device.takeSnapshot()
	
	result = resultado_obtido.sameAs(resultado_esperado, 0.9)
	
	if(result):
		return ('\033[32m'+'Passou'+'\033[0;0m', "O botao esta funcionando corretamente")
	else:
		return ('\033[31m'+'Nao Passou'+'\033[0;0m', "O botao nao possui o comportamento esperado")
	

def aux_ct156(device, vc):
	device.press("KEYCODE_APP_SWITCH", "DOWN_AND_UP") 
  	time.sleep(2)
	
	resultado = device.takeSnapshot()
	
	return resultado

def ct156(device, vc):
	'''
	Test Item: SW BUTTON Home Button
	Action: Use the Recents button and check if it is working
	Result: Recents button is working
	'''
	
	resultado_esperado = aux_ct156(device, vc)
	
	device.press("KEYCODE_HOME", "DOWN_AND_UP")
	
	device.press("KEYCODE_APP_SWITCH", "DOWN_AND_UP") 
  	time.sleep(2)
  	
  	resultado_obtido = device.takeSnapshot()	
  	time.sleep(2)

	result = resultado_obtido.sameAs(resultado_esperado, 0.9)
	
	if result:
		return ('\033[32m'+'Passou'+'\033[0;0m', "O botao esta funcionando corretamente")
	else:
		return ('\033[31m'+'Nao Passou'+'\033[0;0m', "O botao nao possui o comportamento esperado")
	
	
def ct154(device, vc):
    '''
    Test Item: Back Button
    Action: Use the Back button and check if it is working
    Expected Result: Back button is working
    '''    
    
    device.touch(163, 451, "DOWN_AND_UP")
    time.sleep(2)
    
    resultado_esperado = device.takeSnapshot()
    time.sleep(2)
    
    device.press("KEYCODE_CALCULATOR", "DOWN_AND_UP")
    time.sleep(2)
    
    device.press('KEYCODE_BACK', 'DOWN_AND_UP')
    time.sleep(2)
    
    resultado_obtido = device.takeSnapshot()

    if resultado_obtido.sameAs(resultado_esperado, 0.9):
        return ('\033[32m'+'Passou'+'\033[0;0m','O botao esta funcionando corretamente')
    else:
        return ('\033[31m'+'Nao Passou'+'\033[0;0m', "O botao nao apresenta o comportamento esperado")
	
	
def tearDown(device):
	device.press("KEYCODE_HOME", "DOWN_AND_UP")

print 'Conexao'
NomeDoEmulador = "emulator-5554" #"emulator-<NumeroDeSerie>"
tempoMaximoDeConexao = 30 #segundos
device = MonkeyRunner.waitForConnection(tempoMaximoDeConexao, NomeDoEmulador)

print 'ConexaoFIM'

#Criando um Objeto View Client para utilizar a biblioteca
print
print 'Criando um Objeto View Client para utilizar a biblioteca (pode demorar)'
#vc = ViewClient(device, NomeDoEmulador)
vc = True

if vc:
    print '\t>>Objeto Criado!'
else:
    print '\t>>O objeto nao foi criado.'
    sys.exit(0)
print


suite = [ct156, ct58, ct155, ct154]
for i in suite:
    print i(device, vc)[0]
    tearDown(device)
