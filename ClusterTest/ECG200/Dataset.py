import matplotlib.pyplot as plt
import linecache
import csv


def getData():
    filename = r"F:\TimeSeriesDataset\ECG200\ECG200_TRAIN.ts"
    data_list = []
    result_list = []
    for i in range(15, 115):
        line = linecache.getline(filename, i).strip()
        # print(line)
        if not line:
            break
        line_list = list(map(str, line.split(":")))
        data_list.append(list(map(float, line_list[0].split(","))))
        result_list.append(list(map(str, line_list[1])))

    print(data_list)
    print(result_list)
    return data_list, result_list


def writeInCsv(data_list):
    with open(r"F:\TimeSeriesDataset\ECG200\ECG200_TRAIN.csv", "a", newline="", encoding='utf-8', errors='ignore') as f:
        csv_writer = csv.writer(f)
        row_list = []
        for i in range(len(data_list[0])):
            tmp_list = [i+1]
            for data in data_list:
                tmp_list.append(data[0])
            row_list.append(tmp_list)
        # print(row_list)

        for row in row_list:
            csv_writer.writerow(row)
    f.close()



if __name__ == '__main__':
    a, b = getData()
    writeInCsv(a)
