
import pyperclip


def report_to_log():

    content = pyperclip.waitForNewPaste()

    # if clipboard is empty, return
    if content == '':
        print('Clipboard is empty')
        return False

    # if clipboard is not empty, split it into lines
    lines = content.split('\r')

    # if len(lines[0].split()) != 8:
    #     print('Invalid format - 1')
    #     return False

    output_lines = []

    for line in lines:
        row = line.split()
        if len(row) != 8:
            print('Invalid format - 2')
            return False

        result = f'{row[0]}\t\t\t\t{row[6]}\t{row[5]}\t{row[2]}\t{format_duration(row[3])}'
        output_lines.append(result)

    pyperclip.copy('\n'.join(output_lines))

    return True


def format_duration(entry):

    hmsf_list = entry.split(":")

    while len(hmsf_list) < 3:
        hmsf_list.insert(0, "00")

    hmsf_list = [str(item).zfill(2) for item in hmsf_list]

    if len(hmsf_list) == 2:
        hmsf_list.insert(0, "0")

    return ":".join(hmsf_list)


if __name__ == '__main__':

    while True:

        if report_to_log():
            print(pyperclip.paste())


