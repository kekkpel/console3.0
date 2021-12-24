import os
import sys
import subprocess as sub
import ssh_com

nome ='kek'
console_path = nome + '-$'
lista = []
lista_comandi = ['crdir','crf','clear','open','ls','cd','cat','exit','del','help','deldir','python','fhvir','ssh']

global program_dir
program_dir = os.getcwd()

def clear():
    if os.name =='nt':
        os.system('cls')

def help(self,command='help'):
    if command=='help':
        print('')
        print('List of all commands and usage')
        print('cat    |   view the text in a file')
        print('cd     |   change directory')
        print('clear  |   clear the console')
        print('crdir  |   create a directory')
        print('crf    |   create a file')
        print('del    |   delete files')
        print('deldir |   delete a dir')
        print('exit   |   exit the console')
        print('help   |   shows this message')
        print('open   |   open custom apps or windows app')
        print('python |   opens the python shell or runs a .py file')
        print('ssh    |   connect to a device using ssh')
        print('')
        print('fshell version 0.3 -- do not steal this :)')
        print('')
    elif command=='cat':
        print('')
        print('cat [file_name] .. [path_to_file]')
        print('')
        print(' cat is used to view the text inside of a file')
        print(' ex. cat test.txt')
        print('')
    elif command=='cd':
        print('cd [directory_name] .. [path]')
        print('')
        print(' cd is used to change directory')
        print(' ex. cd test')
        print('')
    elif command=='clear':
        print('')
        print('clear')
        print('')
        print(' used to clear the console')
        print('')
    elif command=='crdir':
        print('')
        print('crdir [directory_name]')
        print('')
        print(' used to create a directory')
        print(' ex. crdir directory')
        print('')
    elif command=='crf':
        print('')
        print('crf [file_name]')
        print('')
        print(' create any tipe of file format')
        print(' ex. crf test.py    or    crf test.txt')
        print('')
    elif command=='del':
        print('')
        print('del [file_name]')
        print('')
        print(' delete a single file')
        print(' ex. del test.py    or del test.txt')
        print('')
    elif command=='deldir':
        print('')
        print('deldir [directory_name]')
        print('')
        print(' delete a single directory')
        print(' ex. deldir test')
        print('')
    elif command=='exit':
        print('')
        print('exit')
        print('')
        print(' bro it just exit the program')
        print('')
    elif command=='open':
        print('')
        print('open [app_name]')
        print('')
        print(' special apps made by me:')
        print(' -notes     simple notepad, to open it type-> open notes')
        print(' -clicker   simple autoclicker or spammer, to open type-> open clicker')
        print('')
        print(' or you can just open another app made by windows')
        print('')
    elif command=='ssh':
        print('')
        print('ssh {user@ip}')
        print('')
        print(' connect to a device using ssh')
        print(' ex. ssh root@1.1.1.1')
        print('')


def open_app(self, app_name):
    current_dir = os.getcwd()
    path = program_dir+'\\apps'
    os.chdir(str(path))
    #print(os.getcwd())
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
    print(os.getcwd())


def ls():
    files_dir = os.listdir()
    for i in files_dir:
        print(i)

def directory():
    path = os.getcwd()
    with os.scandir(path) as itr:
        for i in itr:
            if i.is_dir():
                print(i, '<DIR>')
            else:
                print(i, '<FILE>')


def create_files(self, name):
    f = open(name, 'x')
    f.close()

def create_dir(self, name):
    os.mkdir(name)

def cat(self, mode, name, string=None):
    a = list(mode)
    a.remove('-')
    modalita = a[0]
    f = open(name, modalita)
    x = 0
    if mode=='-r':
        for i in f:
            x +=1
            print(i)
    elif mode=='-w':
        f.write(string)
    f.close()

def delete(self, file_name):
    sub.run(['del', file_name], shell=True)

def deldir(self, dir_name):
    os.removedirs(dir_name)

def python(self, file_name=None):
    def py_with_file():
        for i in range(1):
            if file_name != None:
                print(f'Currently running {file_name}')
                print('')
                sub.run([self, file_name], shell=True)
            break
    def py_only():
        sub.run([self])

    if file_name==None:
        py_only()
    elif file_name!=None:
        py_with_file()

def fhvir():
    a = os.getcwd()
    a = a + '\\virus'
    os.chdir(a)
    #print(os.getcwd())
    sub.run(['python','virus.py'])

def ssh(self, mode_ip):
    ssh_com.main_ssh(self, mode_ip)

while True:
    input_console = input(f'{console_path}')
    lista = input_console.split(' ')
    if lista[0]=='clear':
        clear()

    if lista[0]=='help':
        self = lista[0]
        try:
            command = lista[1]
            help(self,command)
        except:
            help(self)
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
        modalita = lista[1]
        nome_file = lista[2]
        try:
            stringa = lista[3]
            cat(prefisso, modalita, nome_file, stringa)
        except:
            cat(prefisso, modalita, nome_file)

    if lista[0]=='del':
        prefisso = lista[0]
        file_name = lista[1]
        delete(prefisso, file_name)

    if lista[0]=='deldir':
        prefisso = lista[0]
        dir_name = lista[1]
        deldir(prefisso, dir_name)

    if lista[0]=='cd':
        prefisso = lista[0]
        path = lista[1]
        cd(prefisso, path)

    if lista[0]=='python':
        prefisso = lista[0]
        try:
            nome_file = lista[1]
            python(prefisso, nome_file)
        except:
            python(prefisso)

    if lista[0]=='ssh':
        prefisso = lista[0]
        com = lista[1]
        ssh(prefisso, com)

    if lista[0]=='dir':
        directory()

    if lista[0]=='fhvir':
        fhvir()


    elif lista[0] not in lista_comandi:
        print('Error 001, command not found')
