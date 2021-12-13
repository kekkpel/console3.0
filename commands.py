import os
import sys
import subprocess as sub

nome ='kek'
console_path = nome + '-$'
lista = []
lista_comandi = ['crdir','crf','clear','open','ls','cd','cat','exit','del']

def clear():
    if os.name =='nt':
        os.system('cls')

def open_app(self, app_name):
    current_dir = os.getcwd()
    os.chdir('C:/Users/Francesco/Desktop/Console3.0/apps')
    #print(self)
    #print(app_name)
    try:
        os.startfile(app_name)
        os.chdir(current_dir)
    except:
        print('Error 002, app not found')

def cd(self, path):
    if path=='..':
        final_path = []
        cur_dir = str(os.getcwd())
        lista_path = cur_dir.split('\\')
        lista_path.pop()
        #print(cur_dir)
        #print(lista_path)
        final_path = '\\'.join(lista_path)
        #print(final_path)
        os.chdir(final_path)
    else:
        os.chdir(path)
    #files_dir = os.listdir()
    #for i in files_dir:
    #    print(i)
    print(os.getcwd())


def ls():
    files_dir = os.listdir()
    for i in files_dir:
        print(i)

def directory():
    path = os.getcwd()
    for roots,dirs,files in os.walk(path):
        print(dirs, '<DIR>')
        print(files, 'files')
        #print(roots,'numero dir',len(dirs),len(files))

def create_files(self, name):
    f = open(name, 'x')
    f.close()

def create_dir(self, name):
    os.mkdir(name)

def cat(self, name):
    f = open(name, 'r')
    for i in f:
        print(i)
    f.close()

def delete(self, file_name):
    sub.run(['del', 'gianni.txt'], shell=True)

while True:
    input_console = input(f'{console_path}')
    lista = input_console.split(' ')
    if lista[0]=='clear':
        clear()

    if lista[0]=='exit':
        break

    if lista[0]=='open':
        #print(lista)
        prefisso = lista[0]
        app_name = lista[1]
        open_app(prefisso, app_name)

    if lista[0]=='ls':
        ls()

    if lista[0]=='crf':
        prefisso = lista[0]
        file_name = lista[1]
        create_files(prefisso, file_name)

    if lista[0]=='crdir':
        prefisso = lista[0]
        dir_name = lista[1]
        create_dir(prefisso, dir_name)

    if lista[0]=='cat':
        prefisso = lista[0]
        nome_file = lista[1]
        cat(prefisso, nome_file)

    if lista[0]=='del':
        prefisso = lista[0]
        file_name = lista[1]
        delete(prefisso, file_name)

    if lista[0]=='cd':
        prefisso = lista[0]
        path = lista[1]
        cd(prefisso, path)

    if lista[0]=='dir':
        directory()

    elif lista[0] not in lista_comandi:
        print('Error 001, command not found')
