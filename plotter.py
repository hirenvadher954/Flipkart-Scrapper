import csv
import matplotlib.pyplot as plt
with open("Acer Nitro 5 Core i7.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    listDateX = []
    listPriceY = []
    tempList = []
    # print("Type of listDateX")
    # print(type(listDateX))
    # print("Type of listPriceY")
    # print(type(listPriceY))

    for line in csv_reader:  # line returns a list
        if "Time" in line:
            continue
        tempList.append(line)

    print(tempList)  # here we have a list of list containing member lists as date,price pairs
    # print(len(tempList))
    tempList.pop()
    print(len(tempList))

    for i in range(0,len(tempList)):
        listDateX.append(tempList[i][0])

    print(listDateX)

    for i in range(0, len(tempList)):
        listPriceY.append(tempList[i][1])

    print(listPriceY)

    plt.plot(listDateX,listPriceY)
    plt.show()



