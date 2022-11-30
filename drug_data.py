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
    
  # 데이터베이스에 db파일 덮어쓰기(선택 약물 삭제용)
  def editDrugDB(self, newDB):
    newDB.to_csv('db.csv')
    
    
  # 병용금기 약물 검색 및 return
  def getMixCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getUsjntTabooInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']
  
  
  # 특정 연령대 금기 약물 검색 및 return
  def getSpecificAgeCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getSpcifyAgrdeTabooInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']

    
  # 노인 주의 약물 검색 및 return
  def getElderCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getOdsnAtentInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']
  
  
  # 임부 금기 약물 검색 및 return
  def getPragnantCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getPwnmTabooInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']
  
  
  # 용량 주의 약물 검색 및 return
  def getDoseCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getCpctyAtentInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']
  
  
  # 투여기간 주의 약물 검색 및 return
  def getDayCautionDrug(self, ingrNameKor):
    import requests
    import json
    
    ingrNameKorShorten = ingrNameKor[:4]
    
    url = 'http://apis.data.go.kr/1471000/DURIrdntInfoService02/getMdctnPdAtentInfoList01?'
    
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'pageNo': '1',
      'type': 'json',
      'numOfRows': '100',
      'ingrKorName': ingrNameKorShorten
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    return json.loads(content)['body']['items']
  
  
  # 약 상세정보 return
  def getDetailedDrugInfo(self, name):
    import requests
    import xml.etree.ElementTree as ET
    
    url = 'http://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService02/getDrugPrdtPrmsnDtlInq01'
    params = {
      'serviceKey': '4ARJOwbLh8jufyYInZFDNEp0phIdsR0d7ZZP0bqJKwTfQ3cL+Df7zJWkSnYAk+8+jCjn/V9RLSxZ2vNFQ+YHrQ==',
      'type':'xml',
      'pageNo': '1',
      'numOfRows':'50',
      'item_name': name,
      }
    
    response = requests.get(url=url, params=params)
    content = response.text
    root = ET.fromstring(content)

    return root[1][3][0]