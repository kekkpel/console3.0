import subprocess
import os

def main_viruses():

    import rickroll as rick
    print('')
    print('Warning I am making this only for fun')
    print('I am not responsable for what you are going to do')
    print('')
    print('This is a collection of viruses made by me')
    print('These viruses have to be converted to exe to work on other pcs')

    while True:
        input_vir = input("virus-$ ")
        if input_vir=='0':
            rick.main_rickroll()
        if input_vir=='exit':
            break


main_viruses()
