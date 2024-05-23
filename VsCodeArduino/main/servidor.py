import socket

#Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8080         # Porta para o servidor

#Dados a serem enviados para o cliente
dados_do_arduino = b'Dados do Arduino: 123' #TEM Q DESCOBRIR ESSA POHA AQUI 

#Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Associa o socket à porta e ao endereço IP
    s.bind((HOST, PORT))
    #Coloca o socket em modo de escuta
    s.listen()

    print('Aguardando conexões...')

    #Aceita uma conexão quando encontrada
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            #Recebe os dados do cliente (navegador)
            data = conn.recv(1024)
            if not data:
                break
            #Envia os dados do Arduino como resposta HTTP ao cliente
            conn.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n' + dados_do_arduino)

print('Servidor encerrado.')