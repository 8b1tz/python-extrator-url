import re


class ExtratorURL:
    def __init__(self, url):
        self.__url = self.__sanitiza_url(url)
        self.__valida_url()

    def __sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def __valida_url(self):
        if not self.__url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.__url)

        if not match:
            raise ValueError("A URL NÃO É VALIDA")

        print("A URL É VALIDA")

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return f"url: {self.__url} \n base: {self.get_url_base()} \n parâmetros: {self.get_url_parametros()}"

    def __eq__(self, other):
        return self.__url == other.__url
    def get_url_base(self):
        indice_interrogacao = self.__url.find("?")
        url_base = self.__url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.__url.find("?")
        url_parametros = self.__url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, nome_parametro):
        parametro_busca = nome_parametro
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
