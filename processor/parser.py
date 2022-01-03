import xlrd


class Parser:
    def __init__(self, filename):
        self.wb = xlrd.open_workbook(filename)

    def get_z01(self):
        ws = self.wb[0]
        res = [0, 0, 0]
        for i in range(ws.nrows):
            for j in range(ws.ncols):
                if ws.cell_value(i, j) == '本年支出合计':
                    res[0] = (float(ws.cell_value(i, j+7)))
                    res[2] = (float(ws.cell_value(i, j+9)))
                    return res
                if ws.cell_value(i, j) == '本年收入合计':
                    res[1] = (float(ws.cell_value(i, j+4)))
        return res

    def get_z01_pie(self):
        ws = self.wb[0]
        data = [ws.cell_value(i, 4) for i in range(6, 14)]
        ingredients = [ws.cell_value(i, 0) for i in range(6, 14)]
        return data, ingredients

    def get_z01_pie_0(self):
        ws = self.wb[0]
        data = [ws.cell_value(6, 14), ws.cell_value(9, 14)]
        ingredients = ['基本支出', '项目支出']
        return data, ingredients

    def get_cs02(self):
        ws = self.wb.sheet_by_name('CS02 主要指标变动情况表')
        for i in range(ws.nrows):
            for j in range(ws.ncols):
                if str(ws.cell_value(i, j)).find('因公出国（境）费') != -1:
                    return {
                        '因公出国（境）费': ws.cell_value(i, j+2),
                        ws.cell_value(i+1, j).strip(): ws.cell_value(i+1, j+2),
                        ws.cell_value(i+4, j).strip(): ws.cell_value(i+4, j+2),
                    }
        return None

    def get_cs02_1(self):
        ws = self.wb.sheet_by_name('CS02 主要指标变动情况表')
        res = {'培训费': 0, '会议费': 0}
        for i in range(ws.nrows):
            for j in range(ws.ncols):
                if str(ws.cell_value(i, j)).find('培训费') != -1:
                    res['培训费'] = ws.cell_value(i, j+2)
                    break
                if str(ws.cell_value(i, j)).find('会议费') != -1:
                    res['会议费'] = ws.cell_value(i, j+2)
                    break
        return res

    def close(self):
        pass
