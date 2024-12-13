value_breaks = lambda x, before : not all(not i in rules[x] for i in before)

def part1(rules, updates):
    
    all_values_fit = lambda u : all(False if u[i] in rules.keys() and value_breaks(u[i], u[:i]) else True for i in range(1, len(u)))
    return sum( u[len(u)//2] if all_values_fit(u) else 0 for u in updates)



def part2(rule, updates):

     all_values_fit = lambda u : all(False if u[i] in rules.keys() and value_breaks(u[i], u[:i]) else True for i in range(1, len(u)))
     return sum( 0 if all_values_fit(u) else orderAndGetValue(u, rules) for u in updates)


def orderAndGetValue(list, rules):
    
    while not all(not value_breaks(list[i], list[:i]) if list[i] in rules.keys() else True for i in range(1, len(list))):

        idx = 1;
        while not list[idx] in rules.keys() or not value_breaks(list[idx], list[:idx]):
            idx += 1

        dummy = list[idx]

        list[idx] = list[idx-1]
        list[idx-1] = dummy

    return list[len(list)//2]



if __name__=="__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    rules = {}
    updates = []
    fill_rules = True
    for line in lines:
        if line.__eq__(""):
            fill_rules = False
        elif fill_rules:
            rule = [int(x) for x in line.split("|")]
            if rule[0] in rules.keys():
                rules[rule[0]].append(rule[1])
            else:
                rules[rule[0]] = [rule[1]]
        else:
            updates.append([int(x) for x in line.split(",")])

    print("Part 1")
    print(part1(rules, updates))
    print("Part 2")    
    print(part2(rules, updates))
