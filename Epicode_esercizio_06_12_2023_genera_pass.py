import random

def Genera_pass(len_pass: int):
    return ''.join([random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm#.,+-')) for C in range(len_pass)])

if __name__=='__main__':
    num=int(input('Inserire numero Char: '))
    print(f'pass di {num} char= {Genera_pass(int(num))}\n\n')
    print('Test 8 char e 20 char \n')
    print(f'pass di  8 char : {Genera_pass(8)} \npass di 20 char : {Genera_pass(20)}')