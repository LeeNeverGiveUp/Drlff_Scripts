import pdb
import re
# part, block, num


class ffield(object):
    """ Read, Write, ffield file
    usage:
        ff = ffield(path)
    """

    def __init__(self, path):
        self.path = path
        self.nothead = '\s*-?\d+'
        self.sep = '^\s*-?\d+\s*(?:!.*)?$'
        self.annotation = '\s*!.*'

        self.parser()

    def parser(self):
        # read and separate data into parts
        self.parsed = {
            'head': [],
            'data': [],  # part, block, num
            'separter': [],
            'annotation': []
        }

        with open(self.path, 'r') as f:
            data = f.readlines()

        ishead = True
        for index, line in enumerate(data):
            if ishead and not re.match(self.nothead, line):
                self.parsed['head'].append(line)
            else:
                ishead = False
                if re.match(self.annotation, line):
                    self.parsed['annotation'].append((index, line))
                else:
                    if re.match(self.sep, line):
                        self.parsed['separter'].append([line])
                        self.parsed['data'].append([])
                    else:
                        if len(self.parsed['data'][-1]) == 0 and not re.match('\s*-?\d|\s*[A-Z][a-z]?\s+-?\d+\.\d+', line):
                            self.parsed['separter'][-1].append(line)
                        else:
                            self.parsed['data'][-1].append(line.strip().split())

        # clean comments from parsed data
        data_cleaned = list()
        for block in self.parsed['data']:   # every large data block
            data_cleaned.append(list())
            for line in block:      # every line
                data_cleaned[-1].append(list())
                found_comment = False
                for element in line:
                    if not found_comment and element.find('!') == -1:
                        data_cleaned[-1][-1].append(element)
                    elif not found_comment and element.find('!') == 0:
                        found_comment = True
                    elif not found_comment:
                        tmp = element[:element.find('!')]
                        if tmp:
                            data_cleaned[-1][-1].append(tmp)
        self.parsed['data'] = data_cleaned

        # split data into small blocks
        seped = list()
        for block in self.parsed['data']:
            if len(block) > 0:
                seped.append(list())
                linear = True if block[0][0].find('.') >= 0 else False
                if linear:      # One line in ffield file is one real logic line
                    for line in block:
                        seped[-1].append([line])
                else:
                    for line in block:
                        if line[0].find('.') == -1:
                            seped[-1].append(list())
                        seped[-1][-1].append(line)
        self.parsed['data'] = seped


def find(a, b, c, data = ff.parsed['data']):
    block = data[a - 1][b-1] # return a-1, b-1, j, k for block[j][k]
    print('block',block)
    lines = len(block)
    i, j = [0] * 2
    found_flag = False
    print('\n\nloop out i c j lines', i, c, j, lines)
    while i < c and j < lines:# iter block
        line = block[j]
        print('line',line)
        k = 0
        print('\nloop in i c k len(line)', i, c, k, len(line))
        while i < c and k < len(line):
            if  line[k].find('.') >= 0:
                i += 1
                print('judge, i, c', i, c)
                if i == c:
                    print('found', a-1, b-1, j, k)
                    found_flag = True
                    break
            k += 1; print('k+1', k)
        if found_flag:
            break
        j += 1; print('j+1', j)
    print('end')
    print(a-1, b-1, j, k)
    print(data[a-1][b-1][j][k])



def main():
    from drlff.env.io import ffield
    from drlff.conf import files_input

    data = ffield(files_input['ffield'])


if __name__ == '__main__':
    main()
