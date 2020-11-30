#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

from mmmmsql import show_db_all
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class MyPlot:
    def __init__(self):
        self.data = []
        self.meth = []
        self.attr = []
        self.labels = []

        self._loop = asyncio.get_event_loop()

    def load_from_db(self):
        result = self._loop.run_until_complete(show_db_all(self._loop))
        self.data.append(result)
        self._loop.close()

        return self.data

    def autolabel(self, rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        fig, ax = plt.subplots()

        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    def draw_bar(self):
        self.labels.append(self.data[0][0][1])
        self.labels.append(self.data[0][1][1])

        self.meth.append(self.data[0][0][2])
        self.meth.append(self.data[0][1][2])

        self.attr.append(self.data[0][0][3])
        self.attr.append(self.data[0][1][3])

        x = np.arange(len(self.labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, self.meth, width, label='Method')
        rects2 = ax.bar(x + width / 2, self.attr, width, label='Attr')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Class Information')
        ax.set_title('Class with its elements')
        ax.set_xticks(x)
        ax.set_xticklabels(self.labels)
        ax.legend()

        fig.tight_layout()
        plt.show()


    def draw_pie(self):
        self.labels.append(self.data[0][0][1])
        self.labels.append(self.data[0][1][1])

        self.meth.append(self.data[0][0][2])
        self.meth.append(self.data[0][1][2])

        self.attr.append(self.data[0][0][3])
        self.attr.append(self.data[0][1][3])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))  # ax1,ax2 refer to your two pies
        labels = 'Method', 'Attr'
        values = [self.meth[0], self.attr[0]]
        ax1.pie(values, labels=labels, autopct='%1.1f%%')  # plot first pie
        ax1.set_title('Cyclelog')

        labels = 'Method', 'Attr'
        values = [self.meth[1], self.attr[1]]
        ax2.pie(values, labels=labels, autopct='%1.1f%%')  # plot second pie
        ax2.set_title('Ride')

        plt.show()

if __name__ == '__main__':
    a = MyPlot()
    a.load_from_db()
    # a.draw()

    a.draw_pie()