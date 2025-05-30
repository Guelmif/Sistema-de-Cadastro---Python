from incluir_Item import *
from Estoque import *
from Listar_itens import *
from Remover_item import *
from Consultar_item import *


print("Bem vindo ao Sistema de Cadsatro de Itens\n")
print('-'*60)

while True:
    
    print("Digite a opção desejada para realizar uma ação no sistema\n")
    print("1. Cadastrar Item\n")
    print("2. Listar todos os itens em estoque\n")
    print("3. Remover um item do estoque\n")
    print("4. Consultar item\n")
    print("5. Sair\n")
    
    opcao = input("Opção: \n")
    
    match opcao:
        case '1':
            Incluir_item()
        case '2':
            listar_itens()
        case '3':
            remover_item()
        case '4':
            consultar_item()
        case '5':
            break
        



