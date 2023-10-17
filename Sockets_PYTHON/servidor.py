import socket

HOST = '127.0.0.1'
PORT = 8080

print('=== Servidor ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

def trata_opcoes(msg):

    valores = msg.split(sep=':')
    operacao = valores[0]
    caminho = valores[1]

    msg = ''

    if operacao == "LERDIR":
        print('LERDIR:' + caminho)

    elif operacao == "CRIARDIR":
        print('CRIARDIR:' + caminho)

    elif operacao == "EXCLUIRDIR":
        print('EXCLUIRDIR:' + caminho)

    elif operacao == "MOSTRAR":
        print('MOSTRAR:' + caminho)

    return msg

while True:
    msg, cliente = udp.recvfrom(1024)
    trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode(encoding="utf-8"))
    resposta = 'mensagem recebida com sucesso!'
    udp.sendto(resposta.encode(), cliente)
    print('Resposta enviada!')