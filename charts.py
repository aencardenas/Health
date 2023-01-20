import matplotlib.pyplot as plt

def generateBarChart(labels,values):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generatePieChart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()



if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,40,800]
    #generateBarChart(labels,values)
    generatePieChart(labels,values)

