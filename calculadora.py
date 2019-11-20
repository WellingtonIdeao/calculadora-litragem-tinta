class Calculadora:
    __area_paredes: float
    __area_teto: float

#formula do cálculo da area das paredes de um comodo
    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2*(comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

#formula do cálculo da area do teto
    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

#rendimento da tinta 1lt para cada 10m2
    def calcular_litragem_necessaria(self):
        if self.__area_paredes <= 0 or self.__area_teto <= 0:
            print(
                'Não é possível calcular a litragem com os valores informados'
            )
            exit()
        return (self.__area_paredes + self.__area_teto) / 10
