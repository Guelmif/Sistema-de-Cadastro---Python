from Estoque import *

def remover_item():
    
    while True:
        item = input("Digite o nome do item que deseja excluir: ").lower()
        
        if item in estoque:
            del estoque[item]
            print(f"Item {item} foi removido com sucesso!")
            break
        else:
            print("Item não encontrado no estoque, tente novamente")
    
    input("APERTE ENTER PARA CONTINUAR")
    