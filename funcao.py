import os

def nome_oficina ():
    print ("------>>>> Oficina do Cesar <<<<------")

def menu ():
    print ("Código | Item | Preço(R$)")
    print ("1 - Bateria - 200,00R$")
    print ("2 - Pneu - 350,00R$")
    print ("3 - Filtro de Óleo - 50,00R$")
    print ("4 - Pastilha de Freio - 100,00R$")
    print ("5 - Sair do sistema")

valor = 0
quantidade = 0

def escolha (): 
    global valor
    global quantidade
    
    opcao = int(input("Escolhe uma opção:"))
    
    match (opcao):
        case 1:
            quantidade = int(input("Escolha quantos itens você deseja:"))
            print("Adicionando uma bateria")
            valor += (200 * quantidade)
            str(input("Digite Qualquer tecla para continuar"))
            main()
        case 2:
            quantidade = int(input("Escolha quantos itens você deseja:"))
            print ("Adicionando um pneu")
            valor += 350 * quantidade
            str(input("Digite Qualquer tecla para continuar"))
            main()
        case 3:
            quantidade = int(input("Escolha quantos itens você deseja:"))
            print ("Adicionando um Filtro de Óleo")
            valor += 50 * quantidade
            str(input("Digite Qualquer tecla para continuar"))
            main()
        case 4:
            quantidade = int(input("Escolha quantos itens você deseja:"))
            print ("Adicionando uma pastilha de Freio")
            valor += 100 * quantidade
            str(input("Digite Qualquer tecla para continuar"))
            main()
        case 5:
            print ("Saindo do sistema")
            print("O valor total é: ", valor)
        case __:
            print ("Opção inválida! DIgite uma opção válida!")
            main()
def main ():
    os.system('cls')
    nome_oficina()
    menu()
    escolha()

if __name__ == '__main__':
    main()