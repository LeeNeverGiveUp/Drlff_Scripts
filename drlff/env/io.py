import pdb
import re
# part, block, num


class ffield(object):

    def __init__(self, path):
        self.path = path
        self.nothead = '\s*-?\d+'
        self.sep = '^\s*-?\d+\s*(?:!.*)?$'
        self.annotation = '\s*!.*'

        self.parser()

    def parser(self):

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

