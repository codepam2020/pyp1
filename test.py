from drug_data import DrugData
import pandas as pd

dd = DrugData()

name = '마그네스정'

data = dd.getDetailedDrugInfo(name)
print(data)