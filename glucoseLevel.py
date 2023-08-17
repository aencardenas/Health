import csv
import charts

def readCsv(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile,delimiter=',')
        header = next(reader)
        print(header)
        data = []

        for row in reader:
            iterable = zip(header,row)
            pacientDict = {key:value for key,value in iterable}
            data.append(pacientDict)
        

    return data


def avgGlucoseLevel(data,gender):
    newData = data.copy()

    if str(gender).capitalize() == 'Male':

        genderDictList = list(filter(lambda x: x['gender'] == str(gender).capitalize(),newData))

    elif str(gender).capitalize() == 'Female':
        genderDictList = list(filter(lambda x: x['gender'] == str(gender).capitalize(),newData))
    
    pacientID = list(map(lambda y: y['id'],genderDictList))
    pacientGlucose = list(map(lambda x: float(x['avg_glucose_level']),genderDictList))

    dictGlucose = dict(zip(pacientID,pacientGlucose))

    return dictGlucose
    

def classifyPacients(dictionary):
    glucoseLevel = list(dictionary.values())
    normal = list(filter(lambda x: True if x>0 and x<=140 else False,glucoseLevel))
    prediabetes = list(filter(lambda x: True if x>140 and x<=199 else False,glucoseLevel))
    diabetes = list(filter(lambda x: True if x>199 else False,glucoseLevel))

    labels = ['NORMAL','PREDIABETES','DIABETES']
    values = [len(normal),len(prediabetes),len(diabetes)]
    print(values)

    return labels,values

   
   
    


if __name__ == '__main__':
    data = readCsv('./healthcareGlucose.csv')
    gender = input('Type the gender(Male/Female) to consult: ')
    dictionary = avgGlucoseLevel(data,gender)
    labels, values = classifyPacients(dictionary)
    charts.generateBarChart(labels,values)
