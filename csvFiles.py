#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     12/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def processCsvFile():
    path ="C:\Programy\PythonProjects\google_stock_data.csv"
    file = open(path)
    for line in file:
        print(line)

def processCsvFile2():
    path ="C:\Programy\PythonProjects\google_stock_data.csv"
    lines = [line for line in open(path)]

    # all data are strings
    print(lines[0].strip()) # strip() remove preceeding or trailing white space
    print(lines[0].strip().split(',')) # split(',') - splits line by defined separator to array

    print('\nAll together')
    dataset = [line.strip().split(',') for line in open(path)]
    print(dataset[1]) #all data are strings
    # there is still problem if our dataset has values surrounded with quotation marks "data"


# using CSV module
def processCsvFile3():
    import csv
    from datetime import datetime

    print(dir(csv))

    path ="C:\Programy\PythonProjects\google_stock_data.csv"
    file = open(path, newline = '') # we set that newline hast to be empty
    reader = csv.reader(file)

    header = next(reader) # The first line is the header

    #data = [row for row in reader] # read the remaining data
    #print(header)
    #print(data[0])

    data = []
    for row in reader: # setting appropriate datatypes
        #row = [Data, Open, High, Low, Close, Volume, Adj. Close]
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1]) # 'open' is builtin function
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])

        data.append([date, open_price, high, low, close, volume, adj_close])

    # Compute and store daily stock returns
    return_path = "C:\Programy\PythonProjects\google_returns.csv"
    file = open(return_path, 'w')
    writer = csv.writer(file)
    writer.writerow(["Date","Return"])

    for i in range(len(data) - 1):
        todays_row = data[i]
        todays_date = todays_row[0]
        todays_price = todays_row[-1] # last item in array adj_close
        yesterdays_row = data[i+1]
        yesterdays_price = yesterdays_row[-1]

        daily_return = (todays_price-yesterdays_price) / yesterdays_price
        #writer.writerow([todays_date, daily_return])
        formatted_date = todays_date.strftime("%m/%d/%Y")
        writer.writerow([formatted_date, daily_return])

    pass

def main():
    #processCsvFile()
    #processCsvFile2()
    processCsvFile3()
    pass

if __name__ == '__main__':
    main()
