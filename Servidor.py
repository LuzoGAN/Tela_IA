import requests
import socket


def perguntar(questao):
    url = "http://localhost:11434/api/chat"
    data = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": questao}
        ],
        "stream": False
    }

    return requests.post(url, json=data)


[09: 23] Luzo
Gomes
Araujo
Neto


def start_server():
    host = '10.151.7.219'  # Endereço do servidor

    port = 12345  # Porta do servidor

    # Cria um socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Vincula o socket a um endereço e porta específicos

        s.bind((host, port))

        # Começa a escutar por conexões

        s.listen()

        print(f'Servidor iniciado em {host}:{port}. Aguardando conexões...')

        while True:  # Loop infinito para aceitar múltiplas conexões

            # Aceita uma conexão

            conn, addr = s.accept()

            with conn:

                print(f'Conexão estabelecida com {addr}')

                while True:  # Loop infinito para lidar com múltiplas mensagens

                    # Recebe dados do cliente

                    data = conn.recv(1024)

                    if not data:
                        print(f'Conexão encerrada com {addr}')

                        break

                    # Converte os dados recebidos para string

                    message = data.decode()

                    print(f'Mensagem recebida do cliente: {message}')

                    # Envia uma resposta de volta para o cliente

                    pergunta = data.decode()

                    print(pergunta)

                    if pergunta.lower() == "sair":
                        break

                    resposta = perguntar(pergunta)

                    print("Se der 200 a resposta deu boa:", resposta.status_code)

                    # Envia a soma de volta para o cliente

                    conn.sendall(str(resposta.json()['message']['content']).encode())

                    print(str(resposta.json()['message']['content']).encode())

                    response = 'Mensagem recebida!'

                    conn.sendall(response.encode())


if __name__ == '__main__':
    start_server()