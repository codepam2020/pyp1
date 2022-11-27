from drug_data import DrugData

dt = DrugData()

data = dt.getDrugName('타이레놀')
for i in data:
  print(i)