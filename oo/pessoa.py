class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f' Olá'

    @staticmethod
    def metodo_estatico():
        return 42


if __name__ == '__main__':
    rafael = Pessoa(nome='Rafael')
    icaro = Pessoa(rafael, nome='icaro')
    # print(Pessoa.cumprimentar(p))
    print(icaro.cumprimentar())
    print(icaro.nome)
    print(icaro.idade)
    for f in icaro.filhos:
        print(f.nome)
    icaro.sobrenome = 'souza'  # só serve para o icaro
    del icaro.filhos
    icaro.olhos = 1
    print(icaro.__dict__)
    print(rafael.__dict__) #refrencia apenas para atr de instancia
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rafael.olhos)
    print(icaro.olhos)
