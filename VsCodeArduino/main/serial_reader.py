from serial import Serial

# Configurações da porta serial
porta_serial = 'COM7'  # Substitua 'COMX' pela porta serial do seu Arduino
baud_rate = 9600

# Nome do arquivo para salvar os dados
nome_arquivo = '.\log.txt'

# Abre a porta serial
arduino = Serial(porta_serial, baud_rate)

# Abre o arquivo para escrita

while True:
    # Lê uma linha da porta serial
    linha = arduino.readline().decode().strip()
        
    # Escreve a linha no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(linha) + '\n')
        arquivo.close()
        
    # Exibe a linha no terminal
    print(linha)