# part, block, num
class ffield(object):
    def __init__(self, path):
        self.path = path
        self.sep = '^\s*\d+\s*(?:!.*)?$'
        self.annotation = '\s*!.*'

    def parser(self):
        self.parsed = {
                'head' = [],
                'data' = [], # part, block, num
                'separter' = [],
                'annotation' = []
                }

        with open(self.path, 'r') as f:
            data = f.readlines()

        i = 0
        while i < len(data):
            if re.match(self.annotation, data[i]): # annotation
                i += 1

            elif re.match(self.sep, data[i]): # separter found, block seped
                pass




