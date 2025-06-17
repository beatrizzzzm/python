def adicao(numero, numero2):
    return numero + numero2

def subtracao(numero, numero2):
    return numero - numero2

def multiplicacao (numero, numero2):
    return numero * numero2

def divisao (numero, numero2):
    return numero / numero2



#main
numero = int(input("digite o primeiro numero"))
numero = int(input("digite o segundo numero"))

resultadoAdicao = adicao(numero, numero2)
resultadoSubtracao = subtracao(numero, numero2)
resultadoMuliplicacao = multiplicacao(numero, numero2)
resulatdoDivisao = divisao(numero, numero2)

print("Adicao: ", resultadoAdicao)
print("Subtracao:", resultadoSubtracao)
print("Multiplicacao:", resultadoMultiplicacao)
print("divisao; ", resultadoDivisao)
