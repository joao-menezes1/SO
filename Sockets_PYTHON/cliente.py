import socket

HOST = '127.0.0.1'
PORT = 8080

servidor = (HOST, PORT)

print('=== Cliente ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def menu():
    print("Menu:")
    print("1 - Mostrar conteúdo do diretório")
    print("2 - Criar diretório")
    print("3 - Excluir diretório")
    print("4 - Mostrar arquivo")

def trata_opcoes(opcao_digitada, caminho):

    msg = ''
    if opcao_digitada == "1":
        msg = 'LERDIR:' + caminho

    elif opcao_digitada == "2":
        msg = 'CRIARDIR:' + caminho

    elif opcao_digitada == "3":
        msg = 'EXCLUIRDIR:' + caminho

    elif opcao_digitada == "4":
        msg = 'MOSTRAR:' + caminho

    return msg

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    caminho = input('Digite o caminho: ')
    msg = trata_opcoes(opcao, caminho)
    udp.sendto(msg.encode(encoding="utf-8"), servidor)
    resposta_servidor, s = udp.recvfrom(1024)
    print(resposta_servidor.decode(encoding='utf-8', errors='backslashreplace'))
