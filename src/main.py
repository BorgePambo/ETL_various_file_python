import pandas as pd
import os
import glob


# camindo para ler os arquivos
folder_path = 'src\\data\\raw'

# Lista todos os arquivos de Excel
excel_files = glob.glob( os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compativel foi encotrado.!")

else:

    # dataframe = tabela na memória para guardar os connteúdo na memória
    dfs = []

    for excel_file in excel_files:

        try:
            dftempo = pd.read_excel(excel_file)

            file_name = os.path.basename(excel_file)

            dftempo['filename'] = file_name
            
            # Criamos uma nova coluna chamada location
            if 'brasil' in file_name.lower():
                dftempo['location'] = 'br'

            elif 'france' in file_name.lower():
                dftempo['location'] = 'fr'

            elif 'italian' in file_name.lower():
                dftempo['location'] = 'it'


            # Criando uma nova coluna chamanda campanha
            dftempo['Campanha'] = dftempo['utm_link'].str.extract(r'utm_campaign=(.*)')

            # Guarda dados tratados dentro de uma dataframe tratado
            dfs.append(dftempo)


        except Exception as ex:
            print(f'Erro ao ler arquivo {excel_file}: {ex}')


if  dfs:

    # concatena todas as tabelas salavas no dfs em uma única tabela
    result = pd.concat(dfs, ignore_index=True)

    # caminho de saida
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # Confire motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # leva dados de do resultado a serem escritos no motor do excel configurado
    result.to_excel(writer, index=False)

    writer._save()

else:
    print('Nenhum dado para ser salvo')