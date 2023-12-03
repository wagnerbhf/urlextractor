from extratorre import ExtratorRegex
from extratorurl import ExtratorUrl

extrator_url = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print("O tamanho da URL: ", len(extrator_url))

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
ExtratorRegex.buscar_cep(endereco)

url = 'https://www.bytebank.com.br/cambio'
ExtratorRegex.validar_url(url)