import socket

# Configurações do servidor
HOST = '192.168.1.10'  # Endereço IP do servidor
PORT = 8080            # Porta para o servidor

# Lê o conteúdo do arquivo HTML
with open('arduino_data.html', 'r') as file:
    homepage = file.read()

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket à porta e ao endereço IP
s.bind((HOST, PORT))

# Coloca o socket em modo de escuta
s.listen(5)

try:
    print('Aguardando conexões!!!')
    while True:
        conn, addr = s.accept()
        print('Conectado por', addr) #endereço do dispositivo de conexão
        
        data = conn.recv(1024)  # Tamanho do buffer de recebimento

        # Decodifica os dados da solicitação
        request = data.decode()
        print("Solicitação:", request)

        # Separa a solicitação para obter a parte do caminho do arquivo
        parts = request.split(' ')
        path = parts[1]

        # Verifica se a solicitação é GET e a raiz (/)
        if parts[0] == 'GET' and path == '/':
            # Monta a resposta com o código HTML
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type: text/html\r\n'
            response += 'Content-Length: ' + str(len(homepage)) + '\r\n'
            response += '\r\n' + homepage
            
            # Codifica a resposta em bytes
            response = response.encode('ascii', 'ignore')

            # Envia a resposta
            conn.sendall(response)

        # Se a solicitação for para o arquivo log.txt
        elif parts[0] == 'GET' and path == '/log.txt':
            # Lê o conteúdo do arquivo log.txt
            with open('log.txt', 'r') as log_file:
                log_content = log_file.read()

            # Monta a resposta com o conteúdo do arquivo log.txt
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type: text/plain\r\n'
            response += 'Content-Length: ' + str(len(log_content)) + '\r\n'
            response += '\r\n' + log_content
            
            # Codifica a resposta em bytes
            response = response.encode('ascii', 'ignore')

            # Envia a resposta
            conn.sendall(response)
        
        # Fecha a conexão
        conn.close()
except KeyboardInterrupt:
    print('Servidor encerrado.')

# Fecha o socket
s.close()