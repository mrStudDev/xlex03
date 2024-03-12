import os
import django
import json
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xlexapp.settings")
django.setup()

from app_juris_stj.models import STJjurisprudenciaModel

def import_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Lendo o arquivo JSON...")
            data = json.load(file)
            print(f"{len(data)} registros encontrados no arquivo JSON.")
            
            instances = []
            for item in data:
                date_str = item.get('data_formatada')
                
                # Convertendo a string de data para um objeto date
                try:
                    formatted_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
                except ValueError:
                    print(f"Erro ao converter a data: {date_str}")
                    continue

                instance = STJjurisprudenciaModel(
                    id_herdadoSTJ=item.get('id_herdadoSTJ', ''),
                    numeroProcesso=item.get('numeroProcesso', ''),
                    numeroRegistro=item.get('numeroRegistro', ''),
                    siglaClasse=item.get('siglaClasse', ''),
                    descricaoClasse=item.get('descricaoClasse', ''),
                    nomeOrgaoJulgador=item.get('nomeOrgaoJulgador', ''),
                    ministroRelator=item.get('ministroRelator', ''),
                    dataPublicacao=item.get('dataPublicacao', ''),
                    data_formatada=formatted_date,                    
                    ementa=item.get('ementa', ''),
                    tipoDeDecisao=item.get('tipoDeDecisao', ''),
                    dataDecisao=item.get('dataDecisao', ''),
                    decisao=item.get('decisao', ''),
                    jurisprudenciaCitada=item.get('jurisprudenciaCitada', ''),
                    notas=item.get('notas', ''),
                    informacoesComplementares=item.get('informacoesComplementares', ''),
                    termosAuxiliares=item.get('termosAuxiliares', ''),
                    teseJuridica=item.get('teseJuridica', ''),
                    tema=item.get('tema', ''),
                    referenciasLegislativas=item.get('referenciasLegislativas', ''),
                    acordaosSimilares=item.get('acordaosSimilares', ''),
                    meta_description=item.get('meta_description', ''),
                    title=item.get('title', ''),                    
                    keyword=item.get('keyword', ''),
                    slug=item.get('slug', ''),
                )
                instances.append(instance)

            print("Salvando registros no banco de dados...")
            STJjurisprudenciaModel.objects.bulk_create(instances)
            print("Dados importados com sucesso!")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {file_path} não é um JSON válido ou está corrompido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    file_path = "/home/marcosscfloripa/projeto/xlex01/media/uploads/stj_juris_files/Final_data_tratada_data_2024_02.json"
    import_from_json(file_path)
