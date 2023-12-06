def Quadrato(lato):
    return lato*4

def Cechio(r):
   return 2*13.14*r

def Rettangolo(base,altezzza):
   return base*2+altezzza*2


if __name__=='__main__':
    import os 
    print('Segli un optione')
    print('A cechio')
    print('B Quadrato')
    print('C Rettangolo')
    print('inserire Q per uscire')
    input_=input()
    
    if input_=='A':
       r=int(input('inseire il raggio: '))
       Cechio(r)

    if input_=='B':
       lato=int(input('inserire il lato: '))
       print(Quadrato(lato))
       
    if input_=='C':
       base=int(input('inserire la base: '))
       altezza=int(input('inserire l altezza: '))
       print(Rettangolo(base,altezza))
       
    if input_=='Q':
       print('fine del gioco')


