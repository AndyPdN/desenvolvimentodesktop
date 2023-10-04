
agenda_telefonica = {}

while True:
    
    nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    numero_telefone = input(f"Digite o número de telefone para {nome}: ")

    
    agenda_telefonica[nome] = numero_telefone


print("Contatos na agenda telefônica:")
for nome, numero_telefone in agenda_telefonica.items():
    print(f"{nome}: {numero_telefone}")
