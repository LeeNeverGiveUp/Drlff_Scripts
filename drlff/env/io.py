import pdb
import re
from copy import deepcopy
# part, block, num


class ffield(object):
    """ Read, Write, ffield file
    usage:
        ff = ffield(path)
    """

    def __init__(self, path):
        self.path = path
        self._nothead = '\s*-?\d+'
        self._sep = '^\s*-?\d+\s*(?:!.*)?$'
        self._annotation = '\s*!.*'

        self._parser()

    def _parser(self):
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
            if ishead and not re.match(self._nothead, line):
                self.parsed['head'].append(line)
            else:
                ishead = False
                if re.match(self._annotation, line):
                    self.parsed['annotation'].append((index, line))
                else:
                    if re.match(self._sep, line):
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

    def _find(self, a, b, c):
        # return data index, convert params to list
        # self.parsed['data'][a][b][c][d]
        heads = 0
        for i in self.parsed['data'][a-1][b-1][0]:
            if i.find('.') >= 0:
                break
            else:
                heads += 1
        line_length = len(self.parsed['data'][a-1][b-1][0]) - heads
        line_num = len(self.parsed['data'][a-1][b-1])
        if c <= line_length:
            return a-1, b-1, 0, c+heads-1
        elif c > line_length * line_num:
            raise IndexError('Indices out of range, ({a}, {b}, *{c}*) [1, {cc}]'.format(
                a=a,
                b=b,
                c=c,
                cc=line_length*line_num
            ))
        else:
            return a-1, b-1, c//line_length, c % line_length - 1

    def __getitem__(self, key):
        try:
            if len(key) != 3:
                raise KeyError('Length of Index must equal 3, given %d' % len(key))
        except TypeError:
            raise KeyError('Length of Index must equal 3, given %d' % len(key))
        for i in key:
            try:
                int(i)
            except ValueError:
                raise TypeError('Indices must be integers, not {}'.format(type(i)))
        indeces = self._find(*key)
        return float(self.parsed['data'][indeces[0]][indeces[1]][indeces[2]][indeces[3]])

    def __setitem__(self, key, value):
        try:
            float(value)
        except ValueError as e:
            raise ValueError(e)
        try:
            if len(key) != 3:
                raise KeyError('Length of Index must equal 3, given %d' % len(key))
        except TypeError:
            raise KeyError('Length of Index must equal 3, given %d' % len(key))
        for i in key:
            try:
                int(i)
            except ValueError:
                raise TypeError('Indices must be integers, not {}'.format(type(i)))
        indeces = self._find(*key)
        self.parsed['data'][indeces[0]][indeces[1]][indeces[2]][indeces[3]] = '{:8.4f}'.format(value)

    def __str__(self):
        parsed = deepcopy(self.parsed)
        string = list()
        string.append(''.join(parsed['head']))
        string.append(''.join(parsed['separter'][0]))
        for sep, dat in zip(parsed['separter'][1:], parsed['data']):
            for i in dat:
                for j in i:
                    for index, number in enumerate(j):
                        if number.find('.') >= 0:
                            j[index] = '{:>8s}'.format(number)
                    j.append('\n')
                    string.append(' '.join(j))
            string.append(''.join(sep))
        return ''.join(string)


def main():
    from drlff.env.io import ffield
    from drlff.conf import files_input

    data = ffield(files_input['ffield'])
    return data


if __name__ == '__main__':
    main()
