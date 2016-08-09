
from math import *

tela = "\tV e i c u l o s\n"\
    "\t1 - Adicionar\n\t2 - Listar\n\t3"\
    "- Remover\n\t4 - Editar\n\t0 - Sair\n"
    
def main():
   
    print tela
    Lista_Veiculos = iniciar()

    
    while True:

        resposta = input()
        
        if resposta == 1:

            ADD = adicionar()
            Arquivo_Veiculos = open('veiculo.txt', 'a')
            Lista_Veiculos.append(ADD)
            Arquivo_Veiculos.write(str(ADD) + "\n")
            Arquivo_Veiculos.close()


        elif resposta == 2:

            listar(Lista_Veiculos)

        elif resposta == 3:

            Remover(Lista_Veiculos)

        elif resposta == 0:

            Finalizar(Lista_Veiculos)
            print "Finalizado."
            break

        else:
            print "Opcao invalida!"
            print tela

    print "Fazendo logout!"




    
def iniciar():

    Arquivo_Veiculos = open('veiculo.txt', 'r')
    linhas = Arquivo_Veiculos.readlines()
    Lista_Veiculos = []
    for linha in linhas:
        Lista_Veiculos.append(eval(linha))
    Arquivo_Veiculos.close()
    
    return Lista_Veiculos




def Finalizar(lista):
     
    arquivo = open('veiculo.txt', 'r+')
    for item in lista:
        arquivo.writelines(str(item) + '\n')
    arquivo.close()


    
def ALista(Lista_Veiculos):

    print "| ID |    Nome    |  Valor  | Ano de Fabricacao | Ano de Modelo | Montador |" 
    for i in range(1, len(Lista_Veiculos)):

        print "| %d  | " % i,
        print "  %s  |" % Lista_Veiculos[i]["Nome"],
        print "  %d  |" % Lista_Veiculos[i]["Valor"],
        print "  %s  |" % Lista_Veiculos[i]["Ano de Fabricacao"],
        print "  %s  |" % Lista_Veiculos[i]["Ano do Modelo"],
        print "  %d  | " % (i+1),
        print "\n"

        

def listar(Lista_Veiculos):

    valor = ALista(Lista_Veiculos)
    print valor
        
    print tela



def adicionar():

    
    Nome = raw_input("Diga o nome do carro:\n ")
    valor = input("Diga seu preco:\n ")
    Ano_Fab = input("Digite o ano de fabricacao: ")
    Ano_Modelo = input("Digite o ano do modelo: ")
    Montador = 0
    Veiculo = {"Nome": Nome, "Valor": valor, "Ano de Fabricacao": Ano_Fab, "Ano do Modelo": Ano_Modelo}
    print "Registro efetuado com sucesso!"
    print tela

    return Veiculo






def Remover(Lista_Veiculos):

    ALista(Lista_Veiculos)

    indice = input("Digite o indice do veiculo que deseja remover: ")
    removido =  Lista_Veiculos.pop(indice)
    print "Carro: ", removido['Nome'], " removido."
    ALista(Lista_Veiculos)








if __name__ == "__main__":

    main()
