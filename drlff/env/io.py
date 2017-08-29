"""files in and out
usage:
    ffp = io.main() # get ffield selected by params


Classes:
    ffield(path): Read, Write, ffield file
        usage:
            ff = ffield('ffield') # put in the ffield file path
            ff[3, 10, 4] = 15.0 # give value indexed as "params" defined
            val = ff[3, 10, 4] # get the value
            print(str(ff)) # print the standard ffield filetype
            ff.write() # write changes to opened file with the "path"
            ff.reset() # reset the file with backuped file(cp .bak/ffield ffield), to use this, you
                #should backup all input files to ".bak" folder
            ff.reload() # reload ffield parameters from file

    ff_params(params_path, ffield_path):select ff with params defined
        usage:
            ffp = ff_params('params', 'ffield')
            list(ffp)

        methods:
            get_value()
            set_value([1,2,3,4,5])
            reset()
"""
import re
import os
from copy import deepcopy
import shutil
# part, block, num


class ffield(object):
    """ Read, Write, ffield file
    usage:
        ff = ffield('ffield') # put in the ffield file path
        ff[3, 10, 4] = 15.0 # give value indexed as "params" defined
        val = ff[3, 10, 4] # get the value
        print(str(ff)) # print the standard ffield filetype
        ff.write() # write changes to opened file with the "path"
        ff.reset() # reset the file with backuped file(cp .bak/ffield ffield), to use this, you
            #should backup all input files to ".bak" folder
        ff.reload() # reload ffield parameters from file

    methods:
        write: save change to file
        reset: reset ffield file from ".bak" folder
        reload: reload from file
    """

    def __init__(self, path):
        self.path = path
        self._nothead = '\s*-?\d+'
        self._sep = '^\s*-?\d+\s*(?:!.*)?$'
        self._annotation = '\s*!.*'

        self._parse()

    def _parse(self):
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

    def write(self):
        with open(self.path, 'w') as f:
            f.write(self.__str__())

    def reload(self):
        self._parse()

    def reset(self, reload=True):
        paths = os.path.split(self.path)
        backup_path = os.path.join(paths[0], '.bak', paths[1])
        shutil.copy(backup_path, self.path)
        if reload:
            self.reload()

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


class ff_params(object):
    """select ff with params defined
    usage:
        ffp = ff_params('params', 'ffield')
        list(ffp)

        # note: the "+" and "+=" do the same thing, just different in returns
        ffp += [.1] * len(ffp)
        ffp + [.1] * len(ffp)
        ffp.value = [1] * 5

    methods:
        get_value()
        set_value([1,2,3,4,5])
        reset()
    """

    def __init__(self, params_path, ffield_path):
        # read and parse params
        self.params_path = params_path
        with open(params_path, 'r') as f:
            params = f.readlines()
        self._params = list()
        for i in params:
            line = re.split('\s+', i.strip())
            for index, j in enumerate(line):
                if j.find('.') >= 0:
                    line[index] = float(j)
                else:
                    line[index] = int(j)
            self._params.append(line)

        transposed = list(zip(*self._params))

        # params info
        self.indices = tuple(zip(*transposed[:3]))
        self.scale = transposed[3]
        self.range = tuple(zip(*transposed[4:]))

        # ffield data
        self.ff = ffield(ffield_path)

    def __len__(self):
        return len(self.scale)

    def get_value(self):
        return [self.ff[i] for i in self.indices]

    def set_value(self, value, judge=True):
        """If judge if value is in range, returns in range -> True else false
        if not judge always return True
        """
        if len(value) != self.__len__():
            raise ValueError('Length of value is not agree with data')
        in_range = True
        if judge:
            in_range = self.judge(value)
        for index, val in zip(self.indices, value):
            self.ff[index] = val
        self.ff.write()
        return in_range

    def __iadd__(self, other):
        data = self.get_value()
        self.set_value(list(map(lambda x: x[0] + x[1], zip(data, other))))
        return self

    def __add__(self, other):
        data = self.get_value()
        judged = self.set_value(list(map(lambda x: x[0] + x[1], zip(data, other))))
        return judged

    def __isub__(self, other):
        data = self.get_value()
        self.set_value(list(map(lambda x: x[0] - x[1], zip(data, other))))
        return self

    def __sub__(self, other):
        data = self.get_value()
        judged = self.set_value(list(map(lambda x: x[0] - x[1], zip(data, other))))
        return judged

    def judge(self, value):
        '''Judge if the value is out of range
        out of range, return False
        in range, return True
        '''
        for rng, val in zip(self.range, value):
            if val < rng[0] or val > rng[1]:
                return False
        return True

    def reset(self):
        self.ff.reset()

    def __repr__(self):
        return str(self.get_value())

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return iter(self.get_value())

    @property
    def value(self):
        return self.get_value()

    def __setattr__(self, name, value):
        if name == 'value':
            self.set_value(value)
        else:
            self.__dict__[name] = value


def main():
    from drlff.env.io import ffield
    from drlff.conf import files_input
    ffield_path = os.path.join(files_input['dir'], files_input['ffield'])
    params_path = os.path.join(files_input['dir'], files_input['params'])

    ffp = ff_params(params_path, ffield_path)
    return ffp


if __name__ == '__main__':
    main()
