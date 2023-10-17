import socket
from pathlib import Path

HOST = '10.0.4.72'
PORT = 5003

servidor = (HOST, PORT)

print('=== Cliente ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def menu():
    print("Menu:")
    print("1 - Mostrar conteúdo do diretório")
    print("2 - Criar diretório")
    print("3 - Excluir diretório")
    print("4 - Mostrar arquivo")

def trata_opcoes(opcao_digitada):

    valores = opcao_digitada.split()
    opcao = valores[0]
    caminho = valores[1]


    msg = ''
    if opcao == "1":
        msg = 'LERDIR:' + caminho

    elif opcao == "2":
        msg = 'CRIARDIR:' + caminho

    elif opcao == "3":
        msg = 'EXCLUIRDIR:' + caminho

    elif opcao == "4":
        msg = 'MOSTRAR:' + caminho

    return msg

while True:
    menu()
    opcao = input('')
    msg = trata_opcoes(opcao)
    udp.sendto(msg.encode(encoding="utf-8"), servidor)
    resposta_servidor, s = udp.recvfrom(1024)
    print(resposta_servidor.decode(encoding='utf-8', errors='backslashreplace'))