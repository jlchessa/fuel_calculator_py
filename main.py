from calculo import Calculo


def main():

    print("""Calculadora de Combustivél""")

    print("Os combustíveis disponíveis para este cálculo são: ")
    print("         Alcool")
    print("         Gasolina")
    print("         Díesel")

    print("")

    try:
        distancia = float(input('Informe a distância a ser percorrida (KM): '))
        consumo_gasolina = float(input('Informe o consumo médio do veículo utilizando gasolina (Km/L): '))
        consumo_alcool = float(input('Informe o consumo médio do veículo utilizando álcool (Km/L): '))
        consumo_diesel = float(input('Informe o consumo médio do veículo utilizando diesel (Km/L): '))
        valor_gasolina = float(input('Informe o valor atual da gasolina: ' "R$"))
        valor_alcool = float(input('Informe o valor atual do álcool:' "R$"))
        valor_diesel = float(input('Informe o valor atual do diesel:' "R$"))
        calculo = Calculo(consumo_gasolina, consumo_alcool, consumo_diesel, distancia,
                          valor_gasolina, valor_alcool, valor_diesel)
        print(
            calculo.calcular_gasto(distancia, consumo_gasolina, consumo_alcool, consumo_diesel)
        )
    except ValueError as erro:
        print("O valor recebido não é válido")


if __name__ == "__main__":
    main()
