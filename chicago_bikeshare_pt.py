# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#data_list = data_list[1:20]
print(data_list[1:20])

# Vamos mudar o data_list para remover o cabeçalho dele.
#data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for features in data_list[1:20]: 
    print(features[-2]) 

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
    column_list = []
    for i in data[1:]:
        column_list.append(i[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

print(len(column_to_list(data_list, -2)))

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[1:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

male = 0
female = 0
for i in data_list:
    if(i[6]=='Male'):
        male +=1
    elif(i[6]=='Female'):
        female +=1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    
    male = 0
    female = 0
    for i in data_list:
        if i[6]=='Male':
            male +=1
        elif i[6]=='Female':
            female +=1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    answer = "Igual"
    if (count_gender(data_list)[0] > count_gender(data_list)[1] ):
        answer = "Masculino"
    else:
        answer = "Feminino"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

#função para contar os tipos de usuários.
def count_user(data_list):
    """
     Função retornara quantidade de usuarios.
     Retorna:
         uma liasta dos tipos de usuários.
     """    
    customer = 0
    subscriber = 0
    dependent = 0

    #loop para acumular o tipos de usuários
    for i in data_list:
        if i[-3]=='Customer':
            customer +=1
        elif i[-3]=='Subscriber':
            subscriber +=1
        elif i[-3] == 'Dependent':
            dependent +=1
    return [customer, subscriber, dependent]

print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber","Dependent"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User')
plt.xticks(y_pos, types)
plt.title('Quantidade por User')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", (male + female) == len(data_list))
answer = input("Escreva sua resposta aqui.")
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)


#muda a trip_duration_list de string para inteiro
trip_duration_list = list(map(int, trip_duration_list))


def get_min_trip():
    """
     Função encontrar o menor valor da lista trip_duration_list.
     Retorna:
         o menor valor.
     """
    min_trip = int(trip_duration_list[0]) #recebe o dados na posição 0

    #faz o filtro comparando o menor valor da variavel min_trip como a lista
    for item in filter(lambda x: x<=min_trip,trip_duration_list):
        min_trip = item
    return min_trip


def get_max_trip():
    """
     Função encontrar o maior valor.
     Retorna:
         o maior valor.
     """
    max_trip = int(trip_duration_list[0]) #recebe o dados na posição 0
    #faz o filtro comparando o menor valor
    for item in filter(lambda x: x>=max_trip,trip_duration_list):
        max_trip = item
    return max_trip


def get_mean_trip():
    """
        Função encontrar o valor médio da lista.
        Retorna:
            o valor medio.
    """
    #encontra o tamanho da lista
    tamanho_lista = len(trip_duration_list)
    #loop da lista tornando valores inteiros
    lista_inteiros = (int(x) for x in trip_duration_list)
    #soma e divide
    resultado_medio = sum(lista_inteiros) / tamanho_lista
    return resultado_medio

def get_median():
    """
     Função encontrar a mediana dos valores.
     Argumentos:
     Retorna:
         o calculo como resultado do maior valor.

     """
    #ordena a lista
    sortlist = sorted(trip_duration_list)
    #recebe o tamanho da lista
    len_numbers = len(trip_duration_list)

    index = (len_numbers - 1) // 2
    if (len_numbers % 2):
        return sortlist[index] #elemento central
    else:
        return (sortlist[index] + sortlist[index + 1])/2.0 #elemento de duas listas

min_trip  =get_min_trip()
max_trip  =get_max_trip()
mean_trip =get_mean_trip()
median_trip = get_median()

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
# variavel esta recebendo a coluna start_stations
start_stations = column_to_list(data_list, -5)

#Só conjunto retira os repetidos
user_types =  set(start_stations)
 
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
#def new_function(param1: int, param2: str) -> list:
how_many_function = 1
new_function = """
     Função de exemplo com anotações.
     Argumentos:
         param1: O primeiro parâmetro.
         param2: O segundo parâmetro.
     Retorna:
         Uma lista de valores x.

     """
print(new_function * how_many_function )

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = input("Você vai encarar o desafio? (yes ou no) ")
answer = "yes"

def count_items(column_list):
    """
     Função contar os itens.
     Argumentos:
         param1: recebe uma lista de generos.
     Retorna:
         retorna dois valores: tipos de generos e a quantidade que tem cada um
    """

#inicializa o objeto
    item_types = []
#inicializa o ojeto    
    count_items = []
#para que possamos encontrar o typos de informações, transformam em lista
# e o \'set', ele são conjuntos e um deles é remover elemento duplicados de uma sequencia
    item_types =list(set(column_list))
#aqui é criado uma varias para receber o retorno de outra função:
    convert_list_int = count_subtems(item_types, list(column_list) )
    counts = [int(x) for x in convert_list_int] 
    return item_types, counts

def count_subtems(types,counts):
    """
     Função contar os subitens.
     Argumentos:
         param1: recebe uma lista de tipos de dados.
         param2: recebe uma lista geral dos tipos informados.
     Retorna:
         retorna 1 valor: lista do com o total de lista infromado
    """    
    list_sum = []
    for i in range(len(types)):
        list_sum.append(len(list(filter(lambda x: x == types[i], counts))))
    return list_sum


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    #------------- Aqui esta validando a função para as colunas tipos de usuários------------
    [1234339, 4, 317162]
    column_list = column_to_list(data_list, -3)
    type_user, count_user = count_items(column_list)
    print("\nTAREFA 11: Validando as função count_items(), passando como parametro o tipo de usuário")
    print("Tipos de usuario:", type_user, "Counts:", count_user)
    assert len(type_user) == 3, "TAREFA 11: Há 3 tipos usuarios!"
    assert sum(count_user) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"

