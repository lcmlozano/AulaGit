def calcularIMC(peso,altura):
    return (peso/(altura*altura))

def classificarIMC(imc):
    if imc > 18.5 and imc < 25:
        print('Peso ideal')
    else:
        print('Fora do peso ideal')

imc = calcularIMC(95, 1.80)
print(imc)
classificarIMC(imc)
