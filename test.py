import pandas as pd
from drug_data import DrugData
import xml.etree.ElementTree as ET

drugData = DrugData()
drugName = '마그네스정'

# ingrCode = drugData.getDrugIngrCode(drugName)
# ingrNameKor = drugData.getDrugIngrNameKor(drugName)
# drugInfo = pd.DataFrame({'name': drugName, 'ingrCode':[ingrCode], 'ingrNameKor': [ingrNameKor]})

res = drugData.getDetailedDrugInfo(drugName)


name = res.find('EE_DOC_DATA').text

section = res.find('EE_DOC_DATA').find('DOC').find('SECTION')

efficacy = []

for tag in section:
  efficacy.append(tag.get('title'))
  for i in tag:
    efficacy.append("  "+ i.text)
    


print('\n'.join(efficacy))

