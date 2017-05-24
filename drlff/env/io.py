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
        for i in data:
            if ishead and not re.match(self.nothead, i):
                self.parsed['head'].append(i)
            else:
                ishead = False
                if re.match(self.annotation, i):
                    self.parsed['annotation'].append[i]
                else:
                    if re.match(self.sep, i):
                        self.parsed['separter'].append[i]
                        self.parsed['data'].append([])
                    else:
                        if len(self.parsed['data'][-1]) == 0 and not re.match('\s*-?\d|\s*[A-Z][a-z]?\s+-?\d+\.\d+', i):
                            self.parsed['separter'][-1].append(i)
                        else:
                            self.parsed['data'][-1].append(i)


def main():
    import conf

f = ffield('ffield')


if __name__ == '__main__':
    main()
)
)
