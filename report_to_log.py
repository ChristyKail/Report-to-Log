#!/usr/local/bin/python3
import re
import tkinter as tk
import pyperclip

__version__ = '2.0.0'


class ReportToLogApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Report to Log')
        self.geometry('500x400')

        # set column and row weights
        self.columnconfigure(0, weight=1)

        self.button = tk.Button(self, text='Reformat clipboard', command=self.run, width=30, pady=10)
        self.button.grid(row=0, column=0, sticky='ew', padx=25, pady=25)

        self.label = tk.Label(self, text='Copy the "reels" data from a shooting day \n'
                                         'report, then click reformat clipboard', font=('Monaco', 14), pady=10)
        self.label.grid(row=1, column=0, sticky='ew', padx=25, pady=25)

    def run(self):

        result, text = report_to_log()

        if result:

            text = re.sub(r'\t+', '\t', text)
            self.label.config(text=text)
            print(text)


def report_to_log():
    content = pyperclip.paste()

    # if clipboard is empty, return
    if content == '':
        print('Clipboard is empty')
        return False, 'Clipboard is empty'

    # if clipboard is not empty, split it into lines
    lines = content.split('\r')

    output_lines = []

    for line in lines:
        row = line.split()
        if len(row) != 8:
            print('Invalid format - 2')
            return False, 'Invalid format'

        result = f'{row[0]}\t\t\t\t{row[6]}\t{row[5]}\t{row[2]}\t{format_duration(row[3])}'
        output_lines.append(result)

    pyperclip.copy('\n'.join(output_lines))

    return True, '\n'.join(output_lines)


def format_duration(entry):
    hmsf_list = entry.split(":")

    while len(hmsf_list) < 3:
        hmsf_list.insert(0, "00")

    hmsf_list = [str(item).zfill(2) for item in hmsf_list]

    if len(hmsf_list) == 2:
        hmsf_list.insert(0, "0")

    return ":".join(hmsf_list)


if __name__ == '__main__':
    app = ReportToLogApp()
    app.mainloop()
