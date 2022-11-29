import pandas as pd
from drug_data import DrugData

drugData = DrugData()
drugName = '마그네스정'

ingrCode = drugData.getDrugIngrCode(drugName)
ingrNameKor = drugData.getDrugIngrNameKor(drugName)
drugInfo = pd.DataFrame({'name': drugName, 'ingrCode':[ingrCode], 'ingrNameKor': [ingrNameKor]})

print(drugInfo)