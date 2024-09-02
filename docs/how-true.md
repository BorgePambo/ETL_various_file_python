
# O que vamos utilizar
python 
pandas
pip é um gerenciador de pacotes do python

# Conceitos
- Virtual Enviroment

 venv
# criar um ambiente virtual
python -m venv .myvenv

# ativar o ambiente virtual
source .myvenv/scripts/activate

# data raw - todos os dados antes de qualquer processo de polimento ou processamento, é o dado sua forma mais crua

# data ready - é quando o dado passou pelo seu processo de refinamento


# PACOTES UTILIZADOS

pip install pandas
pip install openxls
pip install xlswriter

# TRATAMENTOS DE REGRAS 
- Prezar pela confiabilidade e rasteabilidade dos dados

# ETL é um processo de três Etapas
EXTRACT / TRANSFORM / LOADING
Extração (Extract): Coleta de dados de várias fontes, como bancos de dados, arquivos CSV, APIs, ou outros sistemas. O objetivo é reunir os dados necessários para o processamento.

Transformação (Transform): Processamento e transformação dos dados extraídos para torná-los utilizáveis. Isso pode incluir limpeza, filtragem, agregação, e conversão de formatos para garantir que os dados estejam prontos para análise.

Carga (Load): Armazenamento dos dados transformados em um sistema de destino, como um banco de dados ou data warehouse, onde eles podem ser acessados e analisados.