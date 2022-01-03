import os

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class Output:
    def __init__(self, dirname):
        self.dirname = dirname
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    def plot_bar(self, x, y, title):
        fig, ax = plt.subplots()
        ind = range(len(y))
        ax.set(title=title)
        ax.ticklabel_format(style='plain')
        ax.set_xticks(ind, x)
        for i in ind[-1::-1]:
            rects = ax.bar(i, y[i],
                           align='center',
                           label=x[i])
            ax.bar_label(rects, fmt='%s')
        fig.tight_layout()
        filename = title.split('\n')[0]
        plt.savefig(os.path.join(self.dirname, filename))

    def plot_pie(self, data, ingredients, title):
        fig, ax = plt.subplots(figsize=(8, 4),
                               subplot_kw=dict(aspect="equal"))

        def func(pct, allvals):
            absolute = pct / 100. * np.sum(allvals)
            return "{:.1f}%\n({:.2f} )".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                  loc="lower left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title(title)
        fig.tight_layout()
        filename = title.split('\n')[0]
        plt.savefig(os.path.join(self.dirname, filename))

    def plot_z01(self, x, y):
        self.plot_bar(x, [y[0][0], y[1][0]], '图1：收支预算总计变动情况图\n单位（元）')
        self.plot_bar(x, [y[0][1], y[1][1]], '图2：收入预算执行情况图\n单位（元）')
        self.plot_bar(x, [y[0][2], y[1][2]], '图3：支出预算执行情况图\n单位（元）')
        self.plot_bar(x, [y[0][1], y[1][1]], '图6：收入总计变动情况图\n单位（元）')
        self.plot_bar(x, [y[0][2], y[1][2]], '图7：支出总计变动情况图\n单位（元）')

    def plot_cs02(self, data, data0, year):
        if data is None or data0 is None:
            raise ValueError('Data is None')
        labels = data.keys()
        this_year = [data[k] for k in labels]
        last_year = [data0[k] for k in labels]
        fig, ax = plt.subplots()
        x = np.arange(len(labels))
        title = '图8：“三公”经费支出变动情况图\n单位（元）'
        ax.set(title=title)
        ax.ticklabel_format(style='plain')
        ax.set_xticks(x, labels)
        width = 0.35
        rects1 = ax.bar(x - width / 2, this_year, width, label=str(year))
        rects2 = ax.bar(x + width / 2, last_year, width, label=str(year-1))
        ax.bar_label(rects1, fmt='%s')
        ax.bar_label(rects2, fmt='%s')
        ax.legend()
        fig.tight_layout()
        filename = title.split('\n')[0]
        plt.savefig(os.path.join(self.dirname, filename))

    def plot_cs02_1(self, x, y):
        keys = y[0].keys()
        i = 9
        for key in keys:
            if y[0][key] != 0 or y[1][key] != 0:
                self.plot_bar(x, [y[0][key], y[1][key]],
                              f'图{i}：{key}支出总计变动情况图\n单位（元）')
                i += 1
