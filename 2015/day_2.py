def calc_paper_need(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    a_1 = l*w
    a_2 = w*h
    a_3 = h*l
    t = 2*a_1 + 2*a_2 + 2*a_3
    t += min(a_1, a_2, a_3)
    return t

def convert_for_calc(dimensions):
    l, w, h = "", "", ""
    head = 0
    for letter in dimensions:
        if head == 0 and letter != "x":
            l += letter
        elif head == 1 and letter != "x":
            w += letter
        elif head == 2 and letter != "x":
            h += letter
        if letter == "x":
            head += 1
    return [int(l), int(w), int(h)]

def calc_ribbon_need(dimensions):
    dimensions.sort()
    bow = dimensions[0]*dimensions[1]*dimensions[2]
    wrapping =2*dimensions[0] + 2*dimensions[1]

    return bow + wrapping

total = 0
with open("day_2_input.txt", "r") as f:
    for line in f.readlines():
        total += calc_paper_need(convert_for_calc(line))

print(total)