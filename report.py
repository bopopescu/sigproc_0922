import pandas
from datetime import date

def getStudentNumber():
    data = pandas.read_csv("data.csv", usecols=[0])
    return data

def update(attendace):
    data = pandas.read_csv("data.csv")
    data[date.today()] = attendace
    data.to_csv('data.csv', index=False)



