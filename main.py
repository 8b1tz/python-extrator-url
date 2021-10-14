from extrator_url import ExtratorURL

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(f"O tamanho da url é : {len(extrator_url)}")
print(extrator_url)
print(extrator_url == extrator_url2)