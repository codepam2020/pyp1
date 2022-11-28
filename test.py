from drug_data import DrugData

dt = DrugData()

word = '마그네스1'

n = int(input())

if n ==1:
  print(dt.getDrugName(word))
elif n == 2:
  print(dt.getDrugIngrNameKor('마그네스디정'))