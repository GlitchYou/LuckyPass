#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from re import findall, sub

if '.py' in argv[0]:
    del argv[0]
else:
    del argv[0]
    del argv[0]


def sh(cmd):
    from subprocess import call
    return call(cmd, shell=True)


def rsh(cmd):
    from subprocess import getstatusoutput
    return getstatusoutput(cmd)
    
    
def menput(menus: list, prompt: str, num=30):
	from time import sleep
	
	nu = f'\033[1;94mNúm..\033[m'
	es = f'\033[1;94mESSID\033[m'
	bs = f'\033[1;94mBSSID\033[m'
	
	print(f'{nu:{num}}{es:{num}}{bs:{num}}')

	for i, net in enumerate(menus):
		i += 1
		e = net[1]
		b = net[0]

		i = f'\033[1;91m{i}\033[m'
		e = f'\033[1;91m{e}\033[m'
		b = f'\033[1;91m{b}\033[m'
			
		print(f'{i:{num}}{e:{num}}{b:{num}}')
		
	print()
		
	while True:
		try:
			option = int(input(prompt))
			
		except (ValueError, TypeError):
		
			print('\033[91m',
			      'Erro, digite um número inteiro.',
			      '\033[m', sep='')
			
			sleep(1)
			
		else:
			if 0 < option <= len(menus):
				return menus[option - 1]
			else:
				print('\033[91m',
					  'Erro, digite um número das opções disponiveis.',
					  '\033[m', sep='')
				
				sleep(1)

if argv[0] in ['-h', '--help']:
	sh(f'./lukey.py {argv[0]}')
	exit()

				
test = rsh(f'aircrack-ng {argv[-1]}')

if test[0] == 0:
    hand = argv[-1]
    nets = findall(fr'((?:\w+:)+\w+)\s\s(\S+)', test[1])
    
    # nets = [('00:00:00:00:00:00', 'lista'), ('11:11:11:11:11:11', 'teste')]    
    
    if len(nets) > 1:
    	net = menput(nets, 'Selecione uma das opções: ')
    	
    else:
    	net = nets[0]
    	
    essid = net[1]
    bssid = net[0]
    
    del argv[-1]
else:
    print('\033[31mHandshake não encontrado ou esta sem redes\n',
          '\033[32mExecute: ./main.py [ --mn int | --mx int | --keys int | --wor str | --msk str ] handshake.cap\033[m')
          
    exit()
    
args = ''

for a in argv:
	args += f'{a} '

run = f'./lukey.py {args} | aircrack-ng -w- -e {essid} -b {bssid} {hand} -l Key.txt'

print(f'$ {run}')
sh(run)

