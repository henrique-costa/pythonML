import csv

vendedores = {}
vendas_por_vendedor = {}

with open('cadastro_funcionarios.csv', mode='r', encoding='utf-8') as arquivo_funcionarios:
    leitor = csv.reader(arquivo_funcionarios)   

    # for i, linha in enumerate(leitor, start=1):
    #     print(f"Linha {i}: {linha}")

    for linha in leitor:
        codigo = int(linha[0])
        nome = linha[1]
        salario_bruto = float(linha[2])
        descontos = float(linha[3])
        comissao_percentual = float(linha[4]) / 100  # Convertendo para decimal
        
        vendedores[codigo] = {
            'nome': nome,
            'salario_bruto': salario_bruto,
            'descontos': descontos,
            'comissao_percentual': comissao_percentual,
            'total_vendas': 0.0
        }

with open('cadastro_vendas.csv', mode='r', encoding='utf-8') as arquivo_vendas:
    leitor = csv.reader(arquivo_vendas)

    # for i, linha in enumerate(leitor, start=1):
    #     print(f"Linha {i}: {linha}")
    
    for linha in leitor:
        codigo = int(linha[0])
        valor_venda = float(linha[1])
        
        if codigo in vendedores:
            vendedores[codigo]['total_vendas'] += valor_venda

# Calcular valores finais e exibir resultados
resultados = []
print("Valores a serem pagos aos vendedores:")
print("-" * 40)
for codigo, dados in vendedores.items():
    comissao = dados['total_vendas'] * dados['comissao_percentual']
    valor_pago = dados['salario_bruto'] - dados['descontos'] + comissao
    
    print(f"Código: {codigo} - {dados['nome']}")
    print(f"Salário Bruto: R$ {dados['salario_bruto']:.2f}")
    print(f"Descontos: R$ {dados['descontos']:.2f}")
    print(f"Total de Vendas: R$ {dados['total_vendas']:.2f}")
    print(f"Comissão ({dados['comissao_percentual']*100}%): R$ {comissao:.2f}")
    print(f"Valor a Pagar: R$ {valor_pago:.2f}")
    print("-" * 40)
    
    resultados.append([codigo, valor_pago])

# Gerar arquivo CSV com os resultados
with open('pagamentos_vendedores.csv', mode='w', encoding='utf-8', newline='') as arquivo_pagamentos:
    escritor = csv.writer(arquivo_pagamentos)
    escritor.writerow(['Código Vendedor', 'Valor a Pagar'])
    escritor.writerows(resultados)

print("Arquivo 'pagamentos_vendedores.csv' gerado com sucesso!")