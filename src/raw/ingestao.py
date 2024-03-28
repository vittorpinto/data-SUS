# %%
import urllib.request
from multiprocessing import Pool

from tqdm import tqdm

def get_data_uf_ano_mes(uf, ano, mes):
    url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RD{uf}{ano}{mes}.dbc" #file transfer protocol - nao tem hit limit

    file = f"C:/Users/Joao/Desktop/Github/data-SUS/database/rd/dbc/RD{uf}{ano}{mes}.dbc"

    resp = urllib.request.urlretrieve(url, file)    

def get_data_uf(uf, datas):
    for i in tqdm(datas):
        ano, mes, dia = i.split("-")
        ano = ano[-2:]
        get_data_uf_ano_mes(uf,ano,mes)

ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

datas = ['2023-01-01', '2023-02-01']

# %%
for uf in ufs:
    get_data_uf(uf,datas)