# Script para verificar os tipos de entidades disponíveis no Atlas

# Importando as bibliotecas necessárias
import requests
from requests.auth import HTTPBasicAuth

# Autenticando no Atlas
ATLAS_URL = "http://localhost:21000/api/atlas/v2/types/typedefs"
USERNAME = 'admin' 
PASSWORD = 'admin'

# Fazendo a requisição GET
response = requests.get(ATLAS_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

# Verificando a resposta
if response.status_code == 200:
    typedefs = response.json() # typedefs é o JSON que descreve todos os tipos registrados no Atlas
    print("\n Tipos de Metadados no Apache Atlas: ")

    for entity in typedefs.get("entityDefs", []): # typedefs é onde estão as entidades (ex: Tabelas, Processos ETL, Colunas)
        print(f"- {entity['name']}")

else:
    print(f"Erro ao conectar: {response.status_code}")
    print(response.text)
