import socket


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

        # Aceita uma conexão
        conn, addr = s.accept()

        while True:
            with conn:
                print(f'Conexão estabelecida com {addr}')
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)

                    if not data:
                        break

                    # Converte os dados recebidos para números e calcula a soma
                    num1 = data.decode()
                    soma = num1

                    # Envia a soma de volta para o cliente
                    conn.sendall(str(soma + 'b').encode())


if __name__ == '__main__':
    start_server()
