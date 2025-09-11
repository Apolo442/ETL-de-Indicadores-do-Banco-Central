from loader import save_in_csv
import schedule
import time

import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INDICES_CONFIG = [
    {'nome': 'SELIC', 'codigo': 11},
    {'nome': 'IPCA', 'codigo': 433},
    {'nome': 'DOLAR', 'codigo': 1}
]
BCB_URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/1?formato=json'


def fecth_indice(url: str, codigo: int, nome: str):
    url = url.format(codigo=codigo)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        res = response.json()
        
        if not res or not isinstance(res, list) or not res[0]:
            logging.warning(f"Nenhum dado válido retornado para {nome} ({codigo}) na URL: {url}")
            return {}
        
        indicador = res[0]
        if indicador:
            logging.info(f"{nome.upper()} obtido com sucesso: {indicador}")
            
            data_referencia = indicador['data']
            valor_indicador = indicador['valor']
            nome_indicador = nome
            data = {
                "nome_indicador": nome_indicador,
                "data_referencia": data_referencia,
                "valor_indicador": valor_indicador
            }
            
            if data_referencia is None or valor_indicador is None:
                logging.error(f"Dados incompletos para {nome}: {indicador}")
                return {}
            
            logging.info(f"{nome.upper()} obtido com sucesso: {indicador}")
            
            return data  
        if not res:
            logging.warning(f"Nenhum dado foi retornado para URL: {url}")
            return {}
    except requests.RequestException as e:
        logging.error(f"Erro ao buscar dados de {nome} ({codigo}): {e}")
        return {}
    except Exception as e:
        logging.error(f"Erro inesperado ao processar {nome}")
        return {}
 
 
def main():
    indices = []
    for config in INDICES_CONFIG:
        nome = config['nome']
        codigo = config['codigo']
        data = fecth_indice(BCB_URL, codigo, nome)
        indices.append(data)
    
    df = pd.DataFrame(indices)
    

    save_in_csv(df, "data/")    
    
    return indices

if __name__ == "__main__":
    hora = "08:00"
    logging.info(f"Agendador iniciado. A tarefa será executada todos os dias às {hora}.")
    schedule.every().day.at(hora).do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    