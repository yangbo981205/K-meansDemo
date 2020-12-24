import matplotlib.pyplot as plt
import linecache
import csv


def getData():
    filename = r"F:\TimeSeriesDataset\BeetleFly\BeetleFly_TEST.ts"
    data_list = []
    result_list = []
    for i in range(12, 32):
        line = linecache.getline(filename, i).strip()
        # print(line)
        if not line:
            break
        line_list = list(map(str, line.split(":")))
        data_list.append(list(map(float, line_list[0].split(","))))
        result_list.append(int(line_list[1]))

    # print(data_list)
    # print(result_list)
    return data_list, result_list


def writeInCsv(data_list):
    with open(r"F:\TimeSeriesDataset\BeetleFly\dataset.csv", "a", newline="", encoding='utf-8', errors='ignore') as f:
        csv_writer = csv.writer(f)
        row_list = []
        for i in range(len(data_list[0])):
            tmp_list = [i+1]
            for data in data_list:
                tmp_list.append(data[i])
            row_list.append(tmp_list)
        # print(row_list)

        for row in row_list:
            csv_writer.writerow(row)
    f.close()


def showOriginData(data_list):
    x_list = [x for x in range(len(data_list[0]))]
    plt.figure(figsize=(50, 10))
    plt.title('BeetleFly')
    plt.ylim(-2.5, 2.5)
    plt.grid(True)
    for data in data_list:
        plt.plot(x_list, data, color="red", linestyle="--")
    plt.legend(loc=0)
    plt.show()


def showResultData(data_list):
    x_list = [x for x in range(len(data_list[0]))]
    plt.figure(figsize=(50, 10))
    plt.title('BeetleFly')
    plt.ylim(-2.5, 2.5)
    plt.grid(True)
    for i in range(len(data_list)):
        if i < 10:
            plt.plot(x_list, data_list[i], color="red", linestyle="--")
        else:
            plt.plot(x_list, data_list[i], color="green", linestyle="--")
    plt.show()


if __name__ == '__main__':
    data_list, result_list = getData()
    writeInCsv(data_list)
