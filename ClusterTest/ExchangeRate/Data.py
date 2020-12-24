import matplotlib.pyplot as plt
import pandas as pd

filename = r"F:\TimeSeriesDataset\exchange_rate\exchange_rate.txt"
list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h = [], [], [], [], [], [], [], []
with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line_list = list(map(float, line.split(",")))
        list_a.append(line_list[0])
        list_b.append(line_list[1])
        list_c.append(line_list[2])
        list_d.append(line_list[3])
        list_e.append(line_list[4])
        list_f.append(line_list[5])
        list_g.append(line_list[6])
        list_h.append(line_list[7])
    f.close()
date_list = pd.date_range(start="19900101", periods=7588, freq='1D')


def ShowData():
    plt.figure(figsize=(50, 10))
    plt.title('ExchangeRate')
    plt.ylim(0, 2.5)
    plt.grid(True)
    plt.plot(date_list, list_a, color="red", linestyle="--", label="Australia")
    plt.plot(date_list, list_b, color="darkorange", linestyle="--", label="British")
    plt.plot(date_list, list_c, color="blue", linestyle="--", label="Canada")
    plt.plot(date_list, list_d, color="lime", linestyle="--", label="Switzerland")
    plt.plot(date_list, list_e, color="green", linestyle="--", label="China")
    plt.plot(date_list, list_f, color="pink", linestyle="--", label="Japan")
    plt.plot(date_list, list_g, color="magenta", linestyle="--", label="NewZealand")
    plt.plot(date_list, list_h, color="yellow", linestyle="--", label="Singapore")
    plt.legend(loc=0)
    plt.show()


def showAustralia():
    plt.figure(figsize=(50, 10))
    plt.title('showAustralia')
    plt.ylim(0.48, 1.11)
    plt.grid(True)
    plt.plot(date_list, list_a, color="red", linestyle="--", label="Australia")
    plt.legend(loc=0)
    plt.show()


def showBritish():
    plt.figure(figsize=(50, 10))
    plt.title('showBritish')
    plt.ylim(1.21, 2.11)
    plt.grid(True)
    plt.plot(date_list, list_b, color="darkorange", linestyle="--", label="British")
    plt.legend(loc=0)
    plt.show()


def showCanada():
    plt.figure(figsize=(50, 10))
    plt.title('showCanada')
    plt.ylim(0.61, 1.10)
    plt.grid(True)
    plt.plot(date_list, list_c, color="blue", linestyle="--", label="Canada")
    plt.legend(loc=0)
    plt.show()


def showSwitzerland():
    plt.figure(figsize=(50, 10))
    plt.title('showSwitzerland')
    plt.ylim(0.54, 1.38)
    plt.grid(True)
    plt.plot(date_list, list_d, color="lime", linestyle="--", label="Switzerland")
    plt.legend(loc=0)
    plt.show()


def showChina():
    plt.figure(figsize=(50, 10))
    plt.title('showChina')
    plt.ylim(0.11, 0.24)
    plt.grid(True)
    plt.plot(date_list, list_e, color="green", linestyle="--", label="China")
    plt.legend(loc=0)
    plt.show()


def showJapan():
    plt.figure(figsize=(50, 10))
    plt.title('showJapan')
    plt.ylim(0.005, 0.014)
    plt.grid(True)
    plt.plot(date_list, list_f, color="pink", linestyle="--", label="Japan")
    plt.legend(loc=0)
    plt.show()


def showNewZealand():
    plt.figure(figsize=(50, 10))
    plt.title('showNewZealand')
    plt.ylim(0.89, 0.39)
    plt.grid(True)
    plt.plot(date_list, list_g, color="magenta", linestyle="--", label="NewZealand")
    plt.legend(loc=0)
    plt.show()


def showSingapore():
    plt.figure(figsize=(50, 10))
    plt.title('showSingapore')
    plt.ylim(0.84, 0.52)
    plt.grid(True)
    plt.plot(date_list, list_h, color="yellow", linestyle="--", label="Singapore")
    plt.legend(loc=0)
    plt.show()


def DataSeries():
    data_list = []
    for i in range(7588):
        tmp_list = [list_a[i], list_b[i], list_c[i], list_d[i], list_e[i], list_f[i], list_g[i], list_h[i]]
        data_list.append(tmp_list)
    return pd.DataFrame(data=data_list, index=date_list)


if __name__ == '__main__':
    print(DataSeries())
    ShowData()

