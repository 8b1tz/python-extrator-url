from extrator_url import ExtratorURL

extrator_url = ExtratorURL("bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)