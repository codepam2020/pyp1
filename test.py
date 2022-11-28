from drug_data import DrugData
import pandas as pd

dt = DrugData()

word = '마그네스1'

drugInfo = pd.DataFrame({'name': ['타이레놀'], 'ingrCode': ['M12345'], 'ingrNameKor': ['아세트아미노펜']})

answer = dt.saveDrugDB(drugInfo)