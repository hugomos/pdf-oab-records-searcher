# Script for generating OAB records report in PDFs

O script para geração de relatório de registros OAB em PDFs tem como objetivo extrair informações específicas de arquivos PDF, como os registros OAB, e gerar um relatório detalhado desses registros.

O script utiliza técnicas de análise de texto para buscar padrões nos arquivos PDF e identificar os registros OAB.

O relatório gerado inclue informações como o número do registro, o arquivo PDF em que o registro foi encontrado e a pagina. Essa ferramenta pode ser útil para escritórios de advocacia, departamentos jurídicos ou qualquer pessoa que precise acompanhar os registros OAB em arquivos PDF.

## Instalação

```bash
  git clone https://github.com/hugomos/script-for-generating-oab-records-report-in-pdfs.git
```

ou

```bash
  gh repo clone hugomos/script-for-generating-oab-records-report-in-pdfs
```

Entre no diretório do projeto

```bash
  cd script-for-generating-oab-records-report-in-pdfs
```

Instale as dependências

```bash
  python -m pip install -r requirements.txt
```

## Uso/Exemplos

- Todos os arquivos .pdf devem estar em `assets/pdf`

- **oab_records**: Parametro obrigatorio, os registros oab devem estar entre aspas duplas, separados por virgula, por exemplo:

```bash
python src/main.py oab_records="16537-A/AL,133921/SP,154467-A/RJ,46843-A/RJ"
```

## Autores

- [@hugomos](https://www.linkedin.com/in/hugomos/)

## Suporte

Para suporte, mande um email para vitor_osantos@hotmail.com.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
