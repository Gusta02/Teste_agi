import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px

# carrega os dados do Excel em um DataFrame
excel_file = pd.ExcelFile('data/anexo1.xlsx')
data = pd.read_excel(excel_file, sheet_name='Sheet')

# Filtra os colaboradores com último cargo e status ativo
data_filtered = data[(data['is_ultimo_cargo'] == 'S') & (data['status'] == 'ATV')]

# Cria o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='pie-chart'),
    ]),
    html.Div([
        dcc.Input(id='center-input', type='text', placeholder='Código Centro de Custo'),
        dcc.Graph(id='bar-chart'),
        dcc.Slider(
            id='page-slider',
            min=1,
            max=10,
            value=1,
            marks={i: str(i) for i in range(1, 11)},
            step=1
        ),
        html.Button('Próxima Página', id='page-button', n_clicks=0)
    ])
])

# Função para atualizar os gráficos com base na página selecionada e no código do centro de custo
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('page-slider', 'value'),
     Input('center-input', 'n_submit'),
     Input('page-button', 'n_clicks')],
    [State('center-input', 'value')]
)
def update_graph(page_num, submit_n_clicks, button_n_clicks, center_code):
    # Gráfico de Barras: Contagem de Colaboradores por Centro de Custo
    grouped_data = data_filtered.groupby('codigocentrocusto')['nome'].count().reset_index()
    grouped_data = grouped_data.sort_values(by='nome', ascending=False)
    paginated_data = grouped_data[(page_num - 1) * 10:page_num * 10]

    bar_fig = px.bar(paginated_data, x='nome', y='codigocentrocusto', orientation='h',
                     title=f'Contagem de Colaboradores por Centro de Custo - Página {page_num}',
                     labels={'nome': 'Número de Colaboradores', 'codigocentrocusto': 'Código Centro de Custo'})
    
    # Gráfico de Pizza: Distribuição de Tipos de Cargo por Centro de Custo
    if center_code is not None:
        center_data = data_filtered[data_filtered['codigocentrocusto'] == center_code]
        if not center_data.empty:
            cargo_distribution = center_data['descricaotipocargo'].value_counts().head(15)
            
            pie_fig = px.pie(cargo_distribution, names=cargo_distribution.index, values=cargo_distribution.values,
                             title=f'Distribuição de Tipos de Cargo no Centro de Custo {center_code}')
        else:
            pie_fig = px.pie(title=f'Distribuição de Tipos de Cargo - Centro de Custo {center_code} não encontrado')
    else:
        pie_fig = px.pie(title='Distribuição de Tipos de Cargo')
    
    return bar_fig, pie_fig

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
