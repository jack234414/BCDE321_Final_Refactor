#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
from pip._vendor.webencodings import labels

from mmmmsql import show_db_all
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from abc import ABCMeta, abstractmethod


class diagram_data:
    def __init__(self):
        self.data = []
        self._loop = asyncio.get_event_loop()

    def load_from_db(self):
        result = self._loop.run_until_complete(show_db_all(self._loop))
        self.data.append(result)

        return self.data

class ImageContext(object):
    def __init__(self, image_strategy):
        self.image_strategy = image_strategy

    def produce_image(self, data):
        self.image_strategy.draw_diagram(data)


class ImageStrategy(metaclass=ABCMeta):
    @abstractmethod
    def draw_diagram(self, data):
        pass

class BarImageStrategy(ImageStrategy):

    def __init__(self):
        self.labels = []
        self.meth = []
        self.attr = []

    def draw_diagram(self, data):
        for i in range(len(data[0])):
            self.labels.append(data[0][i][1])

        for i in range(len(data[0])):
            self.meth.append(data[0][i][2])

        for i in range(len(data[0])):
            self.attr.append(data[0][i][3])

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


class PieImageStrategy(ImageStrategy):

    def __init__(self):
        self.labels = []
        self.meth = []
        self.attr = []

    def draw_diagram(self, data):
        for i in range(len(data[0])):
            self.labels.append(data[0][i][1])

        for i in range(len(data[0])):
            self.meth.append(data[0][i][2])

        for i in range(len(data[0])):
            self.attr.append(data[0][i][3])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
        labels = 'Method', 'Attr'
        values = [self.meth[0], self.attr[0]]
        ax1.pie(values, labels=labels, autopct='%1.1f%%')
        ax1.set_title(str(self.labels[0]) + 'Class Elements')

        labels = 'Method', 'Attr'
        values = [self.meth[1], self.attr[1]]
        ax2.pie(values, labels=labels, autopct='%1.1f%%')
        ax2.set_title(str(self.labels[1]) + 'Class Elements')
        plt.show()


if __name__ == '__main__':
    DiagramData = diagram_data()
    data = DiagramData.load_from_db()
    diagram_creator = ImageContext(BarImageStrategy())
    diagram_creator.produce_image(data)

    diagram_creator = ImageContext(PieImageStrategy())
    diagram_creator.produce_image(data)