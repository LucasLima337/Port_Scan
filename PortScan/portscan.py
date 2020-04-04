import sys
import socket

try:
    site = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print('Faltam argumentos!')
    sys.exit()

try:
    lista = open(wordlist).read()
    lista = lista.split()
except:
    print('Wordlist não encontrada!')
    sys.exit()

print('=-=' * 10)
for porta in lista:
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.settimeout(0.3)
    alvo = cli.connect_ex((site, int(porta)))
    if alvo == 0:
        print(f'Porta {porta}: OPEN')
    else:
        print(f'Porta {porta}: CLOSED')
print('=-=' * 10)
