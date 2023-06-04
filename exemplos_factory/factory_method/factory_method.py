from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass


class SecaoPessoa(Secao):
    def __repr__(self):
        return "Seção Pessoal"


class SecaoAlbum(Secao):
    def __repr__(self):
        return "Seção Album"


class SecaoProjeto(Secao):
    def __repr__(self):
        return "Seção Projeto"


class SecaoPublicacao(Secao):
    def __repr__(self):
        return "Seção Publicacao"


class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        self.secoes.append(secao)


class Linkedin(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoa())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao)


class Faceboof(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoa())
        self.add_secao(SecaoAlbum())


if __name__ == "__main__":
    rede_social = input("Qual rede social que criar o perfil?[Linkedin, Facebook]")
    perfil = eval(rede_social)()

    print(f"Criando o perfil no(a) {type(perfil).__name__}")

    print(f"O perfil tem as secoes {perfil.get_secoes()}")
