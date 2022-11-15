class DrugData:
  import pandas as pd
  df = pd.read_csv('/Users/yookjs/Programming/Custom_Program/pyp1/productIngrName.csv')

  # 입력받은 약물이름을 csv파일 속 데이터에서 찾은 후 return
  def getDrugName(self, drugName):
    drugList = []
    for i in range(len(self.df)):
      if drugName in self.df['name'][i]:
        drugList.append(self.df['name'][i])
    return drugList
  
  # 입력받은 약물이름을 주성분 코드로 return
  def getDrugIngrCode(self, drugName):
    ingrs = ''
    for i in range(len(self.df)):
      if drugName == self.df['name'][i]:
        ingrs = self.df['ingrCode'][i]
        
    ingrsList = ingrs.split('///')
    return ingrsList
  
  # 입력받은 약물이름을 주성분 한국명으로 return
  def getDrugIngrNameKor(self, drugName):
    ingrs = ''
    for i in range(len(self.df)):
      if drugName == self.df['name'][i]:
        ingrs = self.df['ingrNameKor'][i]
        
    ingrsList = ingrs.split('///')
    return ingrsList