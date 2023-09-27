#Ideia de texto usando formatação para customizar modelos de carro

modelo = 'Gol'
potencia_cilindro = 1.0
cor = 'Vermelho'
ano_fabric = 2005

texto_custom = 'Temos o modelo {Modelo}, na sua versão {Cilindrada}, na cor {Cor}, com o ano de fabricação de {Fabricacao_Ano}'
format_texto = texto_custom.format(
    Modelo=modelo, Cilindrada=potencia_cilindro, Cor=cor, Fabricacao_Ano=ano_fabric
)
print(format_texto)


