import stddraw
import color


def anzeigen(data1, data2):
    stddraw.setCanvasSize(1500, 800)
    stddraw.clear()
    data3 = data1 + data2
    stddraw.setXscale(min(i[0] for i in data3)-1, max(i[0] for i in data3)+1)
    stddraw.setYscale(min(i[1] for i in data3)-1, max(i[1] for i in data3)+1)
    crosspoints = list(set(data1).intersection(set(data2)))
    for i in range(1, len(data1)):
        if data1[i] in crosspoints:
            stddraw.setPenColor(color.YELLOW)
            stddraw.setPenRadius(0.02)
            stddraw.point(data1[i][0], data1[i][1])
        if i == 1:
            stddraw.setPenColor(color.BLACK)
            stddraw.setPenRadius(0.02)
            stddraw.line(0, 0, data1[i-1][0], data1[i-1][1])
        stddraw.setPenColor(color.BLACK)
        stddraw.setPenRadius(0.02)
        stddraw.line(data1[i-1][0], data1[i-1][1], data1[i][0], data1[i][1])
    for i in range(1, len(data2)):
        if data2[i] in crosspoints:
            stddraw.setPenColor(color.YELLOW)
            stddraw.setPenRadius(0.02)
            stddraw.point(data2[i][0], data2[i][1])
        if i == 1:
            stddraw.setPenColor(color.BLACK)
            stddraw.setPenRadius(0.02)
            stddraw.line(0, 0, data2[i-1][0], data2[i-1][1])
        stddraw.setPenColor(color.BLACK)
        stddraw.setPenRadius(0.02)
        stddraw.line(data2[i-1][0], data2[i-1][1], data2[i][0], data2[i][1])
    stddraw.show()


def read_paths(path):
    with open(path, 'r') as f:
        paths = [line.strip().split(',') for line in f]
    return paths


def increment_xy(data):
    wPlot = []
    xy = [0, 0]
    for i in data:
        for _ in range(int(i[1:])):
            if i[0] == 'U':
                xy[1] += 1
            elif i[0] == 'D':
                xy[1] -= 1
            elif i[0] == 'L':
                xy[0] -= 1
            elif i[0] == 'R':
                xy[0] += 1
            else:
                print('input error')
                break
            wPlot.append(tuple(xy[:]))

    return wPlot


def navigate(paths):
    w1Plot = increment_xy(paths[0])
    w2Plot = increment_xy(paths[1])
    intercepts = list(set(w1Plot).intersection(set(w2Plot)))
    print(intercepts)
    abs_intercepts = [(abs(i[0]), abs(i[1])) for i in intercepts]
    print(min([sum(i) for i in abs_intercepts if sum(i) > 0]))


def best_timing(paths):
    crossing = []
    w1Plot = increment_xy(paths[0])
    w2Plot = increment_xy(paths[1])
    intercepts = list(set(w1Plot).intersection(set(w2Plot)))
    for i in intercepts:
        path1 = w1Plot[:w1Plot.index(i)+1]
        path2 = w2Plot[:w2Plot.index(i)+1]
        crossing.append(len(path1)+len(path2))
    print(min(crossing))


# anzeigen(increment_xy(read_paths("wires2.txt")[0]), increment_xy(read_paths("wires2.txt")[1]))
# navigate(read_paths("wires.txt"))
best_timing(read_paths("wires.txt"))

