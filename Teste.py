a = 1
b = 2
c = 3

d = a+ b + c

print(a)
print(b)
print(c)
print(d)

// cometarios são feitos com #
//para cometar muitas linhas se utilia""" ... """

// and e or se escreve and, or , não é utilizado && ||

// #-*- coding: utf-8 -*- == codigo utilizado para colocar acentos

// ** == exponenciação

//variavel = input(menssagem) -> o usuario insere um valor na variavel , retorna string
// para retornar int utilize int(input())
//PS: funciona no cmd, abrindo o arquivo no cmd atraves do comando python <nome do arquivo>

//-----------Lista-----------------

// insere = a um vetor mas sem a quantidade

//para printar == lista[<onde começar>:<onde parar +1>] ou
//lista[posição que vai printar]
//lista*numero = printa a quantidade de numeros
//lista+lista = printa a soma das duas variaveis


//len(variavel) = conta a quantidade de informações inseridas

//.append(valor) = adiciona
//.index(valor) = mostra posição
// <valor> in <variavel> = localiza o valor
//.count(valor) = conta quantos dos valores inseridos uma variavel tem
//.remove(valor) = remove um valor
//.sort(reverse=True) = inverte os valores da lista 
//.sort() = arruma uma lista em ordem
//variavel = sorted(Lista)
//para deletar = del variavel["string"]

//--------------Dicionario-----------

//variavel = {<chave>:<valor>...} = cria uma associação entre valores
//para adicionar uma nova associação = variavel["chave"]=<valor>
// print( variavel["chave"]) ou print(variavel)
//variavel.items() == tranforma o dicionari em uma tupla
//variavel.values() == Retorna so os valores
//variavel.keyes() == Retorna so as chaves


//---------Tuplas------------

//Diferença da tuplas das listas, não se pode alterar adicionar ou apagar um valor só

//insere = listas

//tupla = tuple(lista) = converte uma lista para tupla

//-----------------if else

// ao inves de se utilizar { se usa :
//if(condição):
        //açõa
//else:
        //ação


// elif(condição) se utiliza dentro de um if = else + if
//if(condição):
        //açõa
//elif(condição):
        //açõa                        
//else:
        //ação
//pass == passara pela tomada de decisão sem fazer nada
                             
//---------------------for pass
// a codição do for não fica entre parenteses
//for letra in nome:
//	print(letra)

//---------while
 //while numero>0:
//	print(numero)
//      numer0 = numero-1

// while True == o while sempre acontecera

//break = termina o ciclo while

//continue volta ao inicio do ciclo, tudo que vem depois do continue não sera chamado
                             
//--------------strings-----------------
                            
// variavel = variavel.lower()== Deixa a string minuscula
// se trocar o lower por upper mudara para maiusculo

//variavel.strip() == remove caracteres especiais e espaços no começo e no fim da variavel 
//variavel.split() == transforma uma string em lista, pode se colaocar algo dentro dos parenteses, exemplo = (r) a string sera separada ao aparecer ma letra r
//variavel.find(valor) == procura o valor na string, retornando sua posição
//variavel.replace(valor, valor novo) == substitui o valor pedido por um novo

//---------------Função--------------------

//Criando
//def Nome(Parametros):
        Comandos

//Chamando
//Nome(Argumentos)

//--------------Arquivos-----------
//variavel = open(nome arquivo) == abre o arquivo
//variavel.close() == fecha o arquivo
//variavel.readlines() e .readline() == le todas as linhas do arquivo armazenando em uma lista , aconselhavel fazer em um for
//variavel.read() == le o arquivo inteiro armazenando em uma variavel

//variavel = open(nome arquivo, "w ou a") == abre o arquivo para escrita
//variavel.write(conteudo a ser escrito) == escreve no documento


//-------------random--------

//import random == nescessario para utilizar
//variavel = random.randint(0, 10) == vai escolher um numeor aleatorio de 0 a 10
// random.seed(1) == sempre dara o mesmo numero
//variavel = random.choice(lista) == escolhe um valor aleatorio de uma lista

//------tratamento de exceção----------

//try:
    print(2/0)
//except:
    print("Não é possivel dividir por 0")

//Ao inves de dar erro no codigo fazendo o programa parar o python ira executar o codigo caso de erro nao ira parar o programa e sim dar uma menssagem de erro

//---------------List Comprehension---------------------
//Adiciona valor a uma lista com base em outra ou não

//lista = [valora_a_adicionar laço condição]
//EX: y = [i**2 for i in x] -- sem condiçao
//EX: y = [i**2 for i in x if i%2==1] -- com condiçao

//-----------------Função enumerate------------
//Pega nome e posição ao mesmo tempo

//for i, nome in enumerate(lista):

        print(i, nome)

//---------------função filter--------------
//Filtra uma lista atraves de uma condição para adicionar a outra lista

//lista = filter(nome_da_função, lista)

//PS: para printa tem que usar print(list(variavel))

//----------------função map------------

//pega uma função e aplica a todos elementos de uma lista

//variavel = map(função , lista)

//variavel = list(variavel) == para poder ler

//-------------função Reduce-----------------

//recebe uma lista e retorna um unico valor para essa lista

//from functools import reduce

//variavel = reduce(função, lista)

//-----------------Função Zip------------------

//contatena duas ou mais listas

//for i, j in zip(lista, lista2):
            print(i,j)
