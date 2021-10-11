class Calculo:

    __distancia: float
    __consumo_gasolina: float
    __consumo_alcool: float
    __consumo_diesel: float
    __valor_gasolina: float
    __valor_alcool: float
    __valor_diesel: float

    def __init__(self, __distancia, __consumo_gasolina, __consumo_alcool, __consumo_diesel,
                 __valor_gasolina, __valor_alcool, __valor_diesel):
        self.__distancia = __distancia
        self.__consumo_gasolina = __consumo_gasolina
        self.__consumo_alcool = __consumo_alcool
        self.__consumo_diesel = __consumo_diesel
        self.__valor_gasolina = __valor_gasolina
        self.__valor_alcool = __valor_alcool
        self.__valor_diesel = __valor_diesel

    def calcular_gasto(self, __distancia, __consumo_gasolina, __consumo_alcool, __consumo_diesel):
        if __distancia <= 0 or __consumo_gasolina <= 0 or __consumo_alcool <= 0 or __consumo_diesel <= 0:
            raise Exception('O valor recebido não pode ser menor ou igual a zero')

        gasto_gasolina = round(
            (__distancia/__consumo_gasolina) * self.__valor_gasolina, 2)

        gasto_alcool = round(
            (__distancia / __consumo_alcool) * self.__valor_alcool, 2)

        gasto_diesel = round(
            (__distancia / __consumo_diesel) * self.__valor_diesel, 2)

        return """"
        O valor total gasto será de:
        Gasolina: R$ {}
        Diesel: R$ {}
        Álcool: R$ {}
        """.format(
            gasto_gasolina, gasto_diesel, gasto_alcool
        )
