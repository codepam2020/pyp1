from drug_data import DrugData

dt = DrugData()

data = dt.getDrugIngrNameKor('타이레놀콜드-에스정')
for i in data:
  print(i)