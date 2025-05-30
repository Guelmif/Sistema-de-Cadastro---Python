from Estoque import estoque

def Incluir_item():
    
    while True:
        nome_item = input("Digite o nome do produto que deseja cadastrar: ").lower()
        quantidade_item = int(input("Digite a quantidade do produto: "))
        
        if nome_item == '' or quantidade_item < 0:
            print("ERRO! O NOME DO PRODUTO OU QUANTIDADE ESTÃO INCORRETOS")
        else:
            estoque[nome_item] = quantidade_item
            input(f"{nome_item} cadastrado com sucesso! (APERTE ENTER PARA CONTINUAR)")
            break
        