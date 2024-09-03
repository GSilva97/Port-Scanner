import socket
import threading 

print('''
8888888b.                   888     .d8888b.           
888   Y88b                  888    d88P  Y88b          
888    888                  888    Y88b.              
888   d88P  .d88b.  888d888 888888  "Y888b.    .d8888b  8888b.  88888b. 
8888888P"  d88""88b 888P"   888        "Y88b. d88P"        "88b 888 "88b
888        888  888 888     888          "888 888      .d888888 888  888
888        Y88..88P 888     Y88b.  Y88b  d88P Y88b.    888  888 888  888
888         "Y88P"  888      "Y888  "Y8888P"   "Y8888P "Y888888 888  888

                      by GS
''') 
print("\n GitHub : https://github.com/GSilva97         *")
print("\n*************************************************")


min_port = 0
max_port = 65535

site = str(input('Digite o site ou IP que deseja realizar o PortScan: '))

tipo = input('Você deseja procurar por algumas portas específicas ou por um intervalo?\n [1] Especificar (separadas por espaço) \n [2] Intervalo ').strip()

portas = []

if tipo == "1":
    portas = list(map(int, input('Digite as portas que deseja testar (separadas por espaço): ').split()))
    portas = [porta for porta in portas if min_port <= porta <= max_port]
elif tipo == "2":
    porta_inicial = int(input('Digite a porta inicial do intervalo: '))
    porta_final = int(input('Digite a porta final do intervalo: '))
    if porta_inicial < min_port:
        porta_inicial = min_port
    if porta_final > max_port:
        porta_final = max_port
    if porta_inicial > porta_final:
        print('Porta inicial maior que porta final. Corrigindo para um intervalo válido.')
        porta_inicial, porta_final = porta_final, porta_inicial
    portas = list(range(porta_inicial, porta_final + 1))
else:
    print('Opção inválida. Execute o script novamente e escolha entre "especificar" ou "intervalo".')
    exit()

portas_abertas = []

def verificar_porta(porta):
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(1)
        resultado = cliente.connect_ex((site, porta))
        if resultado == 0:
            portas_abertas.append(porta)
        cliente.close()
    except Exception as e:
        pass 

threads = []
for porta in portas:
    thread = threading.Thread(target=verificar_porta, args=(porta,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

if portas_abertas:
    print('Portas abertas:')
    for porta in portas_abertas:
        print(f'Porta {porta} está aberta.')
else:
    print('Nenhuma porta aberta encontrada.')
