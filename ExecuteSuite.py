# -*- coding: cp1252 -*-

import time
import sys
import os

sys.path.append(os.getenv('VIEW_CLIENT'))
from viewclient import ViewClient
from com.android.monkeyrunner import MonkeyRunner

sys.path.append('/home/lucas/backup/CQTS/automacao/MonkeyRunner')
from suite_smoke_test_alpha_1 import *

def tearDown(device):
	device.press("KEYCODE_HOME", "DOWN_AND_UP")
	time.sleep(2)

REPORT = '/home/lucas/backup/CQTS/automacao/MonkeyRunner/FirstReport.txt'

NomeDoEmulador = "emulator-5554"
tempoMaximoDeConexao = 30
device = MonkeyRunner.waitForConnection(tempoMaximoDeConexao, NomeDoEmulador)

print 'Criando um Objeto View Client para utilizar a biblioteca (pode demorar)'
vc = ViewClient(device, NomeDoEmulador)
if vc:
    print '\t>>Objeto Criado!'
else:
    print '\t>>O objeto nao foi criado.'
    sys.exit(0)

cts_total = len(SUITE)
cts_success = 0
cts_fail = 0
cts_erro = 0
f = open(REPORT, 'w')
while 1:
    print 'Inicio da Suite de Testes'
    f.write('Suite de Teste: ' + 'Smoke Test' + '\n\n')
    suiteStart = time.time()
    for i in SUITE:
        f.write(i.__name__)
        f.write(i.__doc__.encode('cp1252'))
        f.write('Resultado Obtido: ')
        ctStart = time.time()
        try:
            ans = i(device, vc)
            f.write((ans[0] + ' -- ' + ans[1] + '\n').encode('cp1252'))
            if ans[0] == 'Passou':
                cts_success = cts_success + 1
            else:
                cts_fail = cts_fail + 1
        except:
            cts_erro = cts_erro + 1
            f.write('ERRO\n')
        finally:
        	ctFinish = time.time()
        	tearDown(device)
        f.write((u'Tempo de Execução: ' + str(ctFinish - ctStart) + '\n\n').encode('cp1252'))
    suiteFinish = time.time()
    f.write((u'\nFim da Suite\nTempo Total de Execução: '
            + str(suiteFinish - suiteStart) +
            '\nCasos de Teste:\n\tQuantidade Total: ' + str(cts_total) +
            '\n\tSucessos: ' + str(cts_success) +
            '\n\tFalhas: ' + str(cts_fail) +
            '\n\tErros: ' + str(cts_erro) + '\n').encode('cp1252'))
    print 'Fim da Suite de Testes'
    break
f.close()

