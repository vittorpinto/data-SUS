# %%
import urllib.request
from multiprocessing import Pool

from tqdm import tqdm

import sys

sys.path.insert(0, "../lib/")

import dttools

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

dt_start = "2022-02-01"
dt_stop = "2023-05-01"

datas = dttools.date_range(dt_start, dt_stop, monthly=True)

# %%
for uf in ufs:
    get_data_uf(uf,datas)
# %%
