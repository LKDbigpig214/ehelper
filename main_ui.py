import os
import datetime

import PySimpleGUI as sg

from processor import Processor, __version__


output_path = os.path.join(os.getcwd(), 'output')
this_year = datetime.datetime.now().year - 1
years = list(range(this_year+2, this_year-3, -1))

ic = sg.InputCombo(values=years, default_value=this_year-1,
                   disabled=True)

layout = [[sg.Text('Filename'),
           sg.InputCombo(values=years, default_value=this_year,
                         enable_events=True, key='year'),
           sg.Input(),
           sg.FileBrowse()],
          [sg.Text('Filename'),
           ic,
           sg.Input(),
           sg.FileBrowse()],
          [sg.Text('Output'),
           sg.Input(default_text=output_path, key='output')],
          [sg.OK()]]

window = sg.Window(f'EHelper(v{__version__})', layout)

while True:
    event, values = window.read()
    if event is None:
        break
    if event == 'year':
        ic.update(values['year']-1)
    if event == 'OK':
        if not values['Browse'] or not values['Browse0']:
            sg.popup('请选择两个文件')
            continue
        p = Processor(values['Browse'], values['Browse0'],
                      values['year'], values['output'])
        try:
            p.plot_z01()
            p.plot_z01_pie()
            p.plot_cs02()
            p.plot_cs02_1()
        except Exception as exc:
            sg.popup(str(exc))
        p.close()

window.close()
