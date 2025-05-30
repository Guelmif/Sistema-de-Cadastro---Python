from Estoque import *

def consultar_item():
    item = input("Digite o item que gostaria de consultar: ").lower()
    
    if item in estoque:
        print(f"O item {item} tem {estoque[item]} unidades disponíveis")
        
    input("APERTE ENTER PARA CONTINUAR")