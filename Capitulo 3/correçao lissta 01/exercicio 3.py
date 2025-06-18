def calculadiametro (raio):
    return raio * 2

def calculacircunferencia (pi, raio):
    return 2 * pi * raio

def calculaarea (pi, raio):
    return pi * (raio ** 2)

#main
raio = float(input("Digite o valor do raio:"))
pi = 3.14

diametro = calculadiametro(raio)
circunferencia = calculacircunferencia(pi,raio)
area = calculaarea(pi, raio)

print("Diametro: ", diametro)
print("Circunferencia: ",circunferencia)
print("Area: ",area)
