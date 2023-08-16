
```markdown
# Execução dos Códigos Python

Este repositório contém códigos em Python relacionados às atividades propostas. Siga as instruções abaixo para configurar o ambiente e executar os códigos.

## Passo 1: Criar uma Virtual Environment

Abra o terminal e navegue até o diretório do projeto. Execute o seguinte comando para criar uma virtual environment (ambiente virtual):

```bash
python -m venv nome_da_env
```

Substitua `nome_da_env` pelo nome que você deseja dar à sua virtual environment.

## Passo 2: Ativar a Virtual Environment

No terminal, dentro do diretório do projeto, ative a virtual environment usando o comando apropriado para o seu sistema operacional:

**No Windows:**

```bash
nome_da_env\Scripts\activate
```

**No macOS e Linux:**

```bash
source nome_da_env/bin/activate
```

## Passo 3: Instalar as Bibliotecas

Dentro da virtual environment, instale as bibliotecas necessárias listadas no arquivo `requirements.txt` usando o comando:

```bash
pip install -r requirements.txt
```

## Passo 4: Executar os Arquivos Python

Com a virtual environment ativada e as bibliotecas instaladas, você pode executar os arquivos Python correspondentes às atividades. Navegue até a pasta onde o arquivo `.py` está localizado e utilize o comando:

```bash
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome do arquivo que você deseja executar.

## Passo Extra: Desativar a Virtual Environment

Após concluir as execuções, você pode desativar a virtual environment digitando:

```bash
deactivate
```