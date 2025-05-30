from Estoque import *

def listar_itens():
    if not estoque:
        print("O estoque está vazio!\n")
    else:
        print('-'*50)
        print("ITENS NO ESTOQUE ATUALMENTE:\n")
        for item, quantidade in estoque.items():
            print(f"-{item}: {quantidade}")
    
    input("APERTE ENTER PARA CONTINUAR\n")