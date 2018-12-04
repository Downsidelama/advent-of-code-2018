dimension = 1000

counter = list()

for i in range(dimension):
    counter.append(list())
    for j in range(dimension):
        counter[i].append(0)

with open('input.txt') as f:
    for line in f:
        id = line.split('@')[0].strip()
        line = line.split('@')[1].strip()
        point = line.split(':')[0].strip()
        dim = line.split(':')[1].strip()

        for i in range(int(point.split(',')[1].strip()),
                       int(point.split(',')[1].strip()) + int(dim.split('x')[1].strip())):
            for j in range(int(point.split(',')[0].strip()),
                           int(point.split(',')[0].strip()) + int(dim.split('x')[0].strip())):
                counter[i][j] += 1

with open('input.txt') as f:
    for line in f:
        id = line.split('@')[0].strip()
        line = line.split('@')[1].strip()
        point = line.split(':')[0].strip()
        dim = line.split(':')[1].strip()

        correctId = True
        for i in range(int(point.split(',')[1].strip()),
                       int(point.split(',')[1].strip()) + int(dim.split('x')[1].strip())):
            for j in range(int(point.split(',')[0].strip()),
                           int(point.split(',')[0].strip()) + int(dim.split('x')[0].strip())):
                if counter[i][j] > 1:
                    correctId = False
        if correctId is True:
            print(id)

numberofoverlaps = 0
for line in counter:
    for line2 in line:
        if line2 > 1:
            numberofoverlaps += 1
