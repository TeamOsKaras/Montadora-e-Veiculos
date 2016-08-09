
import ast

tela = "\t---------------------\n\t M o n t a d o r a s\n\t---------------------\n"\
    "\n\t1 - Adicionar\n\t2 - Listar\n\t3"\
    "-  Remover\n\t4 - Editar\n\t5 - Filtrar por\n\t6 - Importar Novas\n\t0 - Sair\n"
    
def main():
    
    print tela
    Lista_Montadora = iniciar()

    
    while True:

        resposta = input()
        
        if resposta == 1:

            ADDs = ADD()
            Lista_Montadora.append(ADDs)

        elif resposta == 2:

            LIST(Lista_Montadora)

        elif resposta == 3:

            REMOVE(Lista_Montadora)

        elif resposta == 4:

            EDIT(Lista_Montadora)

        #elif resposta == 5:

            #IMPORT(Lista_Montadora)

       # elif resposta == 6:

            #FILTRO(Lista_Montadora)

        elif resposta == 0:

            Finalizar(Lista_Montadora)
            print "Finalizado."

            break

        else:
            print "Opcao invalida!"
            print tela

    print "Fazendo logout!"




    
def iniciar():

    Arquivo_Montadora = open('montadoras.CSV', 'r')
    linhas = Arquivo_Montadora.readlines()
    Lista_Montadora = []
    for linha in linhas:
        Lista_Montadora.append(eval(linha)) 
    Arquivo_Montadora.close()
    
    return Lista_Montadora




def Finalizar(lista):
     
    arquivo = open('montadoras.CSV', 'w')
    for item in lista:
        arquivo.writelines(str(item) + '\n')
    arquivo.close()


    
def LIST(Lista_Montadora):

    print "| ID |    Nome    |  Pais  | " 
    for i in range(len(Lista_Montadora)):

        print "| %d  |" % i,
        print " %s    |" % Lista_Montadora[i]["Nome"], 
        print " %s |" % Lista_Montadora[i]["Pais"]

    print tela




def ADD():

    
    Nome = raw_input("Diga o nome da Montadora: ").upper()
    Pais = raw_input("Diga seu pais de origem: ").upper()

    Montadora = {"Nome": Nome, "Pais": Pais}
    print "Registro efetuado com sucesso!"
    print tela

    return Montadora




def REMOVE(Lista_Montadora):

    LIST(Lista_Montadora)

    indice = input("Digite o indice da Montadora que deseja remover: ")
    removido = Lista_Montadora.pop(indice)
    LIST(Lista_Montadora)
    



def EDIT(Lista_Montadora):

    Elemento = input("Digite o numero correspondente ao elemento que deseja substituir:\n\t 1- Nome\n\t 2- Pais")
    if Elemento == 1:
        NomeTirado = raw_input("Digite o nome da montadora que deseja substituir: ").upper()
        novo_nome = raw_input("Digite o novo nome da montadora: ").upper()
        for i in range(len(Lista_Montadora)):

            if Lista_Montadora[i]["Nome"] == NomeTirado:
                Lista_Montadora[i]["Nome"] = novo_nome
                
    if Elemento == 2:
        PaisTirado = raw_input("Digite o Pais da montadora que deseja substituir: ").upper()
        novo_Pais = raw_input("Digite o novo Pais da montadora: ").upper()
        for i in range(len(Lista_Montadora)):

            if Lista_Montadora[i]["Pais"] == PaisTirado:
                Lista_Montadora[i]["Pais"] = novo_Pais
                
            
    return Lista_Montadora 



def IMPORT():

    pass




if __name__ == "__main__":

    main()

