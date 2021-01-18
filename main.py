#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, subprocess
from datetime import datetime
from decouple import config

path_session_name = 'sessions'
sudo_password = config('PASSWORD')

paths = [
    '/home/institucionais',
    '/home/imobiliarias',
]

print('Starting script... \n\n')

now = datetime.now()

for path_name in paths:

    print('Checking if existes the path...' + path_name)
    if(os.path.exists(path_name)):

        projetos = []

        print("Caminho existe")
        for x in os.walk(path_name):
            for y in x[1]:
                if y == path_session_name:
                    # projetos.append(x[0] + '/' + y)
                    print('Trying execute command in ' + x[0] + '/' + y)

                    total_files = subprocess.check_output('find ' + x[0] + '/' + y + ' -type f | wc -l', shell=True).decode('ascii').strip()
                    result = subprocess.check_output('echo "' + str(sudo_password) + '" | sudo -S find ' + str(x[0]) + '/' + str(y) + '/ -size 0 -print -delete', shell=True)

                    print('Lets see what\'s left.')
                    total_files_left = subprocess.check_output('find ' + x[0] + '/' + y + ' -type f | wc -l', shell=True).decode('ascii').strip()

                    diferenca = int(int(total_files) - int(total_files_left))
                    print('Was deleted', diferenca, 'files')
                    print(total_files + ' file before - ' + total_files_left + ' files now \n\n')
        
        conteudo_log =  str(now.hour) + ':' + str(now.minute) + ' ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' - ' + 'Prontinho, executado com sucesso. - path: ' + path_name
    else:
        print("Ops, path not exists")
        conteudo_log = str(now.hour) + ':' + str(now.minute) + ' ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' - ' + 'Falha, parece que não econtramos a pasta. - path: ' + path_name
    
    with open("/home/scripts/ClearSessions/log.txt", "a") as log:
        log.write(conteudo_log + "\n")
    