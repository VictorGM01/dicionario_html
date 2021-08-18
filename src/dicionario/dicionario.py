import io


class DicionarioTags:
    def __init__(self):
        self.__arquivo = io.open("tags.txt", "r", encoding='utf8')
        self.__arquivo_a = io.open("tags.txt", "a", encoding="utf8")

    def mostra_todas_as_tags(self):
        with self.__arquivo as arquivo:
            for linha in arquivo:
                print(linha)

    def adiciona_tag(self, tag):
        funcao = str(input("Digite a função desta tag: "))
        with self.__arquivo_a as arquivo:
            arquivo.write("\n")
            arquivo.write(f"tag: {tag} --->>> Função: {funcao}")
            print(f"Tag: '{tag}' adicionada com sucesso!!")

    def busca_tag(self, tag):
        with self.__arquivo as arquivo:
            for linha in arquivo:
                if tag in linha.split(" --->>>")[0]:
                    busca = linha
                    print(busca)

    def busca_funcao(self, palavra_chave):
        palavra_chave = str(palavra_chave).lower()
        with self.__arquivo as arquivo:
            for linha in arquivo:
                if palavra_chave in linha:
                    busca_funcao = linha
                    print(busca_funcao)
