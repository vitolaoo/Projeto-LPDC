arquivo = open("dados.csv", "r") #abre o arquivo csv
verdadeiro = False #define variavel booliana para evitar erro no sistema ao digitar uma informacao errada
numero = str #define numero como string para criar tela de selecao
numero = '0' #define o valor de numero

while numero != '1' and numero != '2' and numero != '3': #enquanto um numero correto nao for pressionado imprime a tela de escolha
    print('escolha uma das opcoes abaixo')
    print('1 - lista completa')
    print('2 - precipitacao')
    print('3 - temperatura')
    numero = (input()) #aguarda resposta do usuario

#exibicao e armazenamento da lista completa
if numero == '1': 
    verdadeiro = True
    for linha in arquivo: #percorre a lista
        valores = linha.split(';') #define ; como separador
        tupla = (valores[0], valores[1], valores[3], valores[4], valores[5], valores[6], valores[7]) #armazena todos os dados da lista em tupla
        print(tupla) #imprime informcoes

#exibicao e armazenamento dos dados de precipitacao
if numero == '2': 
    print('informe um mes e um ano no formato mm/aaaa')

    valor = str(input()) #declara uma variavel para definir a data

    for linha in arquivo: #percorre a lista
        valores = linha.split(';')  #define ; como separador das informacoes
        if valores[0].endswith(valor) and valor.__contains__('/'): #verifica se a coluna datatermina com mês/ano digitado
            verdadeiro = True
            tupla = (valores[0], valores[1]) #armazena as informacoes de data e precipitacao em tupla
            print(tupla) #imprime informacoes

#exibicao e armazenamento dos dados de temperatura maxima
if numero == '3':
    print('informe um ano no formato aaaa')

    valor = (input())

    for linha in arquivo: #percorre todas as linhas do arquivo csv
        valores = linha.split(';') #separacao das colunas do arquivo csv
        if valores[0].endswith(valor): #compara se a coluna data termina com o ano digitado
        #compara se a coluna data comeca com os 7 primeiros dias de cada mes
            if valores[0].startswith('01') or valores[0].startswith('02') or valores[0].startswith('03') or valores[0].startswith('04') or valores[0].startswith('05') or valores[0].startswith('06') or valores[0].startswith('07'):
                verdadeiro = True #se encontrou resultado
                tupla = (valores[0], valores[2]) #armazenando os valores de data e temperatura para exibicao
                print(tupla)

arquivo.close()

if verdadeiro == False: #se nao encontrou valores exibe a mensagem
    print('nenhum valor encontrado com esses parametros')