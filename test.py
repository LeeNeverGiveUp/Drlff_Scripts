from drlff.env import io
ffield = io.main()
data = ffield.parsed['data']

def find(a, b, c, data):
    heads = 0
    for i in data[a-1][b-1][0]:
        if i.find('.') >= 0:
            break
        else:
            heads += 1
    line_length = len(data[a-1][b-1][0]) - heads
    line_num = len(data[a-1][b-1])
    if c <= line_length:
        return a-1, b-1, 0, c+heads-1
    elif c > line_length * line_num:
        raise IndexError('c is out of range of [1, %d]' % line_length*line_num)
    else:
        return a-1, b-1, c//line_length, c % line_length - 1
