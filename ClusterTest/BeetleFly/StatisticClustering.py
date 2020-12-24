import BeetleFly.Dataset as dataset
import matplotlib.pyplot as plt
import numpy as np
import csv

def dataDeal():
    d_list, r_list = dataset.getData()
    result_list = []

    for data in d_list:
        tmp_list = []
        tmp_list.append(max(data))
        tmp_list.append(min(data))
        tmp_list.append(np.mean(data))
        tmp_list.append(sum(data))
        # tmp_list.append(np.argmax(np.bincount(data)))
        tmp_list.append(0)
        tmp_list.append(np.median(data))
        tmp_list.append(np.var(data))
        tmp_list.append(np.std(data))
        result_list.append(tmp_list)

    # for i in result_list:
    #     print(i)

    # with open(r"F:\TimeSeriesDataset\BeetleFly\similarity.csv", "a", newline="", encoding='utf-8', errors='ignore') as f:
    #     csv_writer = csv.writer(f)
    #     for data in result_list:
    #         csv_writer.writerow(data)
    # f.close()

    return result_list


def clusteringCenter(data_list):
    x = 0.0
    y = 0.0
    z = 0.0
    for data in data_list:
        x += data[0]
        y += data[1]
        z += data[2]
    x = x/len(data_list)
    y = y/len(data_list)
    z = z/len(data_list)
    # a_class = [x-0.1, y-0.1, z-0.1]
    # b_class = [x+0.1, y+0.1, z+0.1]
    a_class = data_list[0]
    b_class = data_list[10]
    return a_class, b_class


def clustering(data_list, a_class, b_class):
    a_list = []
    b_list = []
    for data in data_list:
        dis_a = (data[0]-a_class[0])**2 + (data[1]-a_class[1])**2 + (data[2]-a_class[2])**2
        dis_b = (data[0]-b_class[0])**2 + (data[1]-b_class[1])**2 + (data[2]-b_class[2])**2
        if dis_a >= dis_b:
            b_list.append(data)
        else:
            a_list.append(data)

    a_x = 0
    a_y = 0
    a_z = 0
    for a in a_list:
        a_x += a[0]
        a_y += a[1]
        a_z += a[2]
    a_class = [a_x/len(a_list), a_y/len(a_list), a_z/len(a_list)]

    b_x = 0
    b_y = 0
    b_z = 0
    for b in b_list:
        b_x += b[0]
        b_y += b[1]
        b_z += b[2]
    b_class = [b_x / len(b_list), b_y / len(b_list), b_z / len(b_list)]

    return a_list, b_list, a_class, b_class


if __name__ == '__main__':
    r_l = dataDeal()
    use_list = []
    for da in r_l:
        use_list.append([da[0], da[1], da[5]])
    # print(use_list)
    a_c, b_c = clusteringCenter(use_list)
    for tim in range(8):
        a_l, b_l, a_c, b_c = clustering(use_list, a_c, b_c)
        print("al", a_l)
        print(len(a_l))
        print("bl", b_l)
        print(len(b_l))
        print("ac", a_c)
        print("bc", b_c)


