import BeetleFly.Dataset as dataset
import matplotlib.pyplot as plt
import numpy as np
import csv


# 初始k值为2，确定初始位置
def originK(data_list):
    # 选取所有数据的均值
    avg_result = 0
    for data in data_list:
        avg_result += np.mean(data)
    avg_result = avg_result/len(data_list)

    # 选取数据均值两边的值作为首次迭代的簇
    a_class = [avg_result-1 for i in range(len(data_list[0]))]
    b_class = [avg_result+1 for i in range(len(data_list[0]))]

    # 选取最大和最小两个序列作为首次迭代的簇
    # a_class = data_list[11]
    # b_class = data_list[2]
    return a_class, b_class


# 显示初始数据和初始聚类结果
def originShow(data_list, a_class, b_class):
    x_list = [x for x in range(len(data_list[0]))]
    plt.figure(figsize=(50, 10))
    plt.title('BeetleFlyOrigin')
    plt.ylim(-2.5, 2.5)
    plt.grid(True)
    for data in data_list:
        plt.plot(x_list, data, color="red", linestyle="--")
    plt.plot(x_list, a_class, color="blue", linestyle="-", linewidth=2)
    plt.plot(x_list, b_class, color="blue", linestyle="-", linewidth=2)
    plt.show()


def k_means(data_list, a_class, b_class):
    result = []
    for data in data_list:
        distance_a = 0
        distance_b = 0
        for i in range(len(data)):
            distance_a += (data[i]-a_class[i])**2
            distance_b += (data[i]-b_class[i])**2
        if distance_a >= distance_b:
            result.append(0)
        else:
            result.append(1)

    a_list = []
    b_list = []
    for i in range(len(data_list)):
        if result[i] == 0:
            a_list.append(data_list[i])
        else:
            b_list.append(data_list[i])

    for i in range(len(a_class)):
        avg_a = 0
        avg_b = 0
        for data_a in a_list:
            avg_a += data_a[i]
        if len(a_list) != 0:
            avg_a = avg_a/len(a_list)
        else:
            avg_a = avg_a
        for data_b in b_list:
            avg_b += data_b[i]
        else:
            avg_b = avg_b
        if len(b_list) != 0:
            avg_b = avg_b/len(b_list)
        a_class[i] = avg_a
        b_class[i] = avg_b
    return a_list, b_list, a_class, b_class


# 按步骤显示聚类结果
def showProcess(a_list, b_list, a_class, b_class):
    x_list = [x for x in range(len(a_class))]
    plt.figure(figsize=(50, 10))
    plt.title('BeetleFlyProcess')
    plt.ylim(-2.5, 2.5)
    plt.grid(True)
    for data in a_list:
        plt.plot(x_list, data, color="red", linestyle="--")
    for data in b_list:
        plt.plot(x_list, data, color="green", linestyle="--")
    plt.plot(x_list, a_class, color="red", linestyle="-", linewidth=5, label="a_class_red")
    plt.plot(x_list, b_class, color="green", linestyle="-", linewidth=5, label="b_class_green")
    plt.legend(loc=0)
    plt.show()


# 输出准确率
def accuracyRate(data_list, result_list, a_list, b_list):
    accuracy_rate = 0
    result = []
    for i in range(len(data_list)):
        if data_list[i] in a_list:
            result.append(2)
        elif data_list[i] in b_list:
            result.append(1)
    print(result)

    for i in range(len(data_list)):
        if (data_list[i] in a_list) and result_list[i] == 1:
            accuracy_rate += 1
        if (data_list[i] in b_list) and result_list[i] == 2:
            accuracy_rate += 1
    return accuracy_rate/len(result_list)


if __name__ == '__main__':
    d_list, r_list = dataset.getData()
    a, b = originK(d_list)
    originShow(d_list, a, b)
    a_l, b_l, a_c, b_c = k_means(d_list, a, b)
    showProcess(a_l, b_l, a_c, b_c)
    print("迭代第1轮，准确率为{}%".format(accuracyRate(d_list, r_list, a_l, b_l)*100))
    # print("class A", a_c)
    # print("class B", b_c)
    for j in range(5):
        a_l, b_l, a_c, b_c = k_means(d_list, b_c, a_c)
        showProcess(a_l, b_l, b_c, a_c)
        a_r = accuracyRate(d_list, r_list, a_l, b_l)
        print("迭代第{}轮，准确率为{}%".format(j+2, a_r*100))
        # print("class A", a_c)
        # print("class B", b_c)

    # with open(r"F:\TimeSeriesDataset\BeetleFly\class.csv", "a", newline="", encoding='utf-8', errors='ignore') as f:
    #     csv_writer = csv.writer(f)
    #     for i in range(len(class_list[0])):
    #         row = []
    #         for data in class_list:
    #             row.append(data[i])
    #         csv_writer.writerow(row)
    # f.close()



