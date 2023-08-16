import pandas as pd

# caminho do arquivo Excel
excel_file = pd.ExcelFile('data/anexo1.xlsx')

# transforma os dados da planilha em dataframe
data = pd.read_excel(excel_file, sheet_name='Sheet')
# print(data)

# Filtra os dados para incluir apenas os últimos cargos
data_filtered1 = data[data['is_ultimo_cargo'] == 'S']

# Filtra os colaboradores com status ativo = ATV
data_filtered = data_filtered1[data_filtered1['status'] == 'ATV']

# Realize os joins para cada nível de gestor
result = data_filtered.merge(data_filtered, left_on='gestornome', right_on='nome', suffixes=('', '_gestor2'))
result = result.merge(data_filtered, left_on='gestornome_gestor2', right_on='nome', suffixes=('', '_gestor3'))
result = result.merge(data_filtered, left_on='gestornome_gestor3', right_on='nome', suffixes=('', '_gestor4'))
result = result.merge(data_filtered, left_on='gestornome_gestor4', right_on='nome', suffixes=('', '_gestor5'))

# Selecione as colunas desejadas no resultado final
final_result = result[['codigocentrocusto', 'nome', 'descricaotipocargo', 'gestornome', 'gestornome_gestor2', 'gestornome_gestor3', 'gestornome_gestor4', 'gestornome_gestor5']]

# Exiba o resultado
# print(final_result)

output_file = 'data/resultado_pandas.xlsx'
final_result.to_excel(output_file, index=False)

print(f"Resultado salvo em {output_file}")
