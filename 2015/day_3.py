def calc_at_least_one_present(directions):
    current = [0, 0]
    current2 = [0, 0]
    houses = {(0,0): 2}
    for j, i in enumerate(directions):
        if j%2 == 0:
            if i == "<":
                current[0] -= 1
            elif i == ">":
                current[0] += 1
            elif i == "^":
                current[1] += 1
            elif i == "v":
                current[1] -= 1
        else:
            if i == "<":
                current2[0] -= 1
            elif i == ">":
                current2[0] += 1
            elif i == "^":
                current2[1] += 1
            elif i == "v":
                current2[1] -= 1   
        
        if (current[0], current[1]) in houses:
            houses[(current[0], current[1])] += 1
        else:
            houses[(current[0], current[1])] = 1        
        if (current2[0], current2[1]) in houses:
            houses[(current2[0], current2[1])] += 1
        else:
            houses[(current2[0], current2[1])] = 1
    return len(houses)


print(calc_at_least_one_present("^><^>>>^"))
