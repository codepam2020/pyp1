import pandas as pd
class DrugData:
  df = pd.read_csv('./productIngrName.csv')

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
        break
      
    ingrsList = ingrs.split('///')
    return ingrsList
  
  # 입력받은 약물이름을 주성분 한국명으로 return
  def getDrugIngrNameKor(self, drugName):
    ingrs = ''
    for i in range(len(self.df)):
      if drugName == self.df['name'][i]:
        ingrs = self.df['ingrNameKor'][i]
        break
      
    ingrsList = ingrs.split('///')
    return ingrsList
  
  # 선택된 약물을 데이터베이스에 저장
  def saveDrugDB(self, drugInfo):
    try:
      db = pd.read_csv('db.csv', index_col=0)
      db = db.append(drugInfo, ignore_index=True)
      db.to_csv('db.csv')
    except:
      db = drugInfo
      db.to_csv('db.csv')
  
  # 데이터베이스에서 복용 약물 리스트 return
  def readDrugDB(self):
    try:
      db = pd.read_csv('db.csv', index_col=0)
      return db
    except:
      pass
    
