import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Carregue os dados do Excel em um DataFrame
excel_file = pd.ExcelFile('data/anexo1.xlsx')
data = pd.read_excel(excel_file, sheet_name='Sheet')

# Filtra os colaboradores com último cargo e status ativo
data_filtered = data[(data['is_ultimo_cargo'] == 'S') & (data['status'] == 'ATV')]

# Agrupa os dados pelo código do centro de custo e conta o número de colaboradores
grouped_data = data_filtered.groupby('codigocentrocusto')['nome'].count().reset_index()
grouped_data.rename(columns={'nome': 'num_colaboradores'}, inplace=True)

# Ordena os dados por número de colaboradores em ordem decrescente
grouped_data = grouped_data.sort_values(by='num_colaboradores', ascending=False)

# Define o número de centros de custo a serem exibidos por página
items_per_page = 10

# Cria uma lista de DataFrames, cada um representando uma página de centros de custo
pages = [grouped_data[i:i+items_per_page] for i in range(0, len(grouped_data), items_per_page)]

# Cria o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    dcc.Graph(id='bar-chart'),
    dcc.Slider(
        id='page-slider',
        min=0,
        max=len(pages) - 1,
        value=0,
        marks={i: str(i+1) for i in range(len(pages))},
        step=1
    )
])

# Função para atualizar o gráfico com base na página selecionada
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('page-slider', 'value')]
)
def update_bar_chart(page_num):
    page_data = pages[page_num]
    fig = px.bar(page_data, x='num_colaboradores', y='codigocentrocusto', orientation='h',
                 title=f'Centros de Custo por Número de Colaboradores - Página {page_num + 1}',
                 labels={'num_colaboradores': 'Número de Colaboradores', 'codigocentrocusto': 'Código Centro de Custo'})
    return fig

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
