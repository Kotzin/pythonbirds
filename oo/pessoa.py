class Pessoa:
    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f' Olá'


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
    print(icaro.__dict__)
    print(rafael.__dict__)
