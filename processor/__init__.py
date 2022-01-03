import os

from .parser import Parser
from .output import Output

__version__ = '0.0.1'

class Processor:
    def __init__(self, file1=None,
                 file2=None,
                 year=None,
                 save_path=None):
        self.file1 = file1
        self.file2 = file2
        self.wb1 = Parser(file1)
        self.wb2 = Parser(file2)
        self.year = year
        save_path = os.path.join(
            save_path,
            os.path.basename(file1).split('.')[0])
        self.output = Output(save_path)

    def close(self):
        self.wb1.close()
        self.wb2.close()

    def plot_z01(self):
        x = [self.year, self.year-1]
        y = [self.wb1.get_z01(),
             self.wb2.get_z01()]
        self.output.plot_z01(x, y)

    def plot_z01_pie(self):
        data, ingredients = self.wb1.get_z01_pie()
        self.output.plot_pie(data, ingredients,
                             '图4：收入决算结构图\n单位（元）')
        data, ingredients = self.wb1.get_z01_pie_0()
        self.output.plot_pie(data, ingredients,
                             '图5：支出决算结构图\n单位（元）')

    def plot_cs02(self):
        data1 = self.wb1.get_cs02()
        data2 = self.wb2.get_cs02()
        self.output.plot_cs02(data1, data2, self.year)

    def plot_cs02_1(self):
        x = [self.year, self.year-1]
        y = [self.wb1.get_cs02_1(),
             self.wb2.get_cs02_1()]
        self.output.plot_cs02_1(x, y)
