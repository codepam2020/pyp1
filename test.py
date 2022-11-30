import pandas as pd
from drug_data import DrugData
import xml.etree.ElementTree as ET

drugData = DrugData()

db = drugData.readDrugDB()

# 병용금기 약물
def findMixDrug():

    cautionDrugList = []
    cautionIngrList = []

    for i in range(len(db)):
        ingrNameKorList = eval(db["ingrNameKor"][i])
        for ingrNameKor in ingrNameKorList:
            try:
                cautionList = drugData.getMixCautionDrug(ingrNameKor)
                for item in cautionList:
                    cautionIngrList.append(item["item"]["MIXTURE_ORI"])

            except:
                pass

    for i in range(len(db)):
        ingrCodeList = eval(db["ingrCode"][i])
        for ingrCode in ingrCodeList:
            for j in cautionIngrList:
                if ingrCode in j:
                    cautionDrugList.append(db["name"][i])
                    break

    cautionDrugList = list(set(cautionDrugList))

    return "\n".join(cautionDrugList)


# 특정 연령대 금기 약물
def findSpecificAgeCautionDrug():
    specificAgeCautionDrugList = []

    for i in range(len(db)):
        ingrList = eval(db["ingrNameKor"][i])
        for item in ingrList:
            try:
                drugData.getSpecificAgeCautionDrug(item)[0]["item"]
                specificAgeCautionDrugList.append(db["name"][i])
            except:
                pass

    specificAgeCautionDrugList = list(set(specificAgeCautionDrugList))

    return "\n".join(specificAgeCautionDrugList)


# 노인 복용 금기 약물
def findElderCautionDrug():
    elderCautionDrugList = []
    for i in range(len(db)):
        ingrList = eval(db["ingrNameKor"][i])
        for item in ingrList:
            try:
                drugData.getElderCautionDrug(item)[0]["item"]
                elderCautionDrugList.append(db["name"][i])
            except:
                pass

    elderCautionDrugList = list(set(elderCautionDrugList))

    return "\n".join(elderCautionDrugList)


# 임부 복용 금기 약물
def findPragnantCautionDrug():
    pragnantCautionDrugList = []
    for i in range(len(db)):
        ingrList = eval(db["ingrNameKor"][i])
        for item in ingrList:
            try:
                drugData.getPragnantCautionDrug(item)[0]["item"]
                pragnantCautionDrugList.append(db["name"][i])
            except:
                pass

    return "\n".join(pragnantCautionDrugList)


# 용량 주의 약물
def findDoseCautionDrug():
    doseCautionDrugList = []
    for i in range(len(db)):
        ingrList = eval(db["ingrNameKor"][i])
        for item in ingrList:
            try:
                drugData.getDoseCautionDrug(item)[0]["item"]
                doseCautionDrugList.append(db["name"][i])
            except:
                pass

    doseCautionDrugList = list(set(doseCautionDrugList))

    return "\n".join(doseCautionDrugList)


# 기간 주의 약물
def findDayCautionDrug():
    dayCautionDrugList = []
    for i in range(len(db)):
        ingrList = eval(db["ingrNameKor"][i])
        for item in ingrList:
            try:
                drugData.getDayCautionDrug(item)[0]["item"]
                dayCautionDrugList.append(db["name"][i])
            except:
                pass

    dayCautionDrugList = list(set(dayCautionDrugList))

    return "\n".join(dayCautionDrugList)


print(findDayCautionDrug())
