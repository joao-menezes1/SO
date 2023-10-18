import socket
from pathlib import Path

HOST = '127.0.0.1'
PORT = 8080

print('=== Servidor ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

def lista_arquivos(caminho):
    arquivos = []
    caminho_arquivo = Path(caminho)
    if caminho_arquivo.is_dir():
        for item in caminho_arquivo.iterdir():
            if item.is_file():
                arquivos.append(f"Arquivo: {item.name}")
            elif item.is_dir():
                arquivos.append(f"Pasta: {item.name}")
        return arquivos
    else:
        return [f"{caminho} não é um diretório válido."]

def trata_opcoes(msg):
    valores = msg.split(sep=':')
    operacao = valores[0]
    caminho = valores[1]

    if operacao == "LERDIR":
        resposta = lista_arquivos(caminho)
        return '\n'.join(resposta)

    elif operacao == "CRIARDIR":
        caminho_arquivo = Path(caminho)
        caminho_arquivo.mkdir()
        return "Diretório criado com sucesso."

    elif operacao == "EXCLUIRDIR":
        caminho_arquivo = Path(caminho)
        try:
            caminho_arquivo.rmdir()
            return "Diretório removido com sucesso."
        except FileNotFoundError:
            return f"{caminho} não existe ou não é um diretório vazio."

    elif operacao == "MOSTRAR":
        try:
            with open(caminho, 'r') as arquivo:
                return arquivo.read()
        except FileNotFoundError:
            return f"{caminho} não foi encontrado."

while True:
    msg, cliente = udp.recvfrom(1024)
    resposta = trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode(encoding="utf-8"))
    udp.sendto(resposta.encode(), cliente)
    print('Resposta enviada!')
