def fibonacci(num):
    # Função auxiliar para calcular a sequência de Fibonacci até que o número seja encontrado ou ultrapassado
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


def is_fibonacci(numero):    # Verifica se o número pertence à sequência de Fibonacci
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

is_fibonacci(4)
is_fibonacci(2)
is_fibonacci(3)

