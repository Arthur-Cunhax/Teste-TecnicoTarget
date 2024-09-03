#Sequência de Fibonacci começa por 0 e 1 e vai somando
lista = [0,1]
numero = int(input("Digite um número para verificarmos se está dentro da Sequência de Fibonacci: \n"))
#Soma dos dois últimos valores
while lista[-1] < numero:
    soma = lista[-1] + lista[-2]
    lista.append(soma)
#Verificando se o valor está dentro da Sequência de Fibonacci
if lista[-1] == numero or numero == 0:
    print("O número digitado pelo usuário durante a execução do programa está na Sequência de Fibonacci")
elif lista[-1] != numero:
    print("O número digitado pelo usuário durante a execução do programa NÃO está na Sequência de Fibonacci")