import json 

def calcular_faturamento(faturamento_diario):
    # Filtrando os valores para ignorar os dias sem faturamento
    faturamento_filtrado = [item['valor'] for item in faturamento_diario if item['valor'] > 0]

    if not faturamento_filtrado:
        return None, None, 0  # Se não houver dias válidos

    # Cálculo do menor e maior faturamento
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)

    # Cálculo da média mensal
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

    # Cálculo do número de dias acima da média
    dias_acima_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media


# Dados de faturamento em formato JSON
dados_json = '''
[
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
'''

# Carregar os dados JSON
faturamento_diario = json.loads(dados_json)


menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

# Saída dos resultados
print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")