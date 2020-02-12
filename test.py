import csv
with open("result.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    listOfAttributes = []
    listOfData = []
    indexOfTitle = 0
    indexOfData = 0
    counter = 0
    for line in csv_reader:
        if counter == 0:
            listOfAttributes = line

        if counter == 1:
            listOfData = line

        counter +=1
    #
    # for line in csv_reader:
    #     if "title" in line:
    #         indexOfTitle = line.index("title")
    #
    #     if "data" in line:
    #         indexOfData = line.index("data")
    #
    # print(indexOfTitle, indexOfData)
    #