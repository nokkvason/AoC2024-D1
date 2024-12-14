import re


with open('input.txt', 'r') as file:
    pattern = re.compile(r'mul\([0-9]+\,[0-9]+\)')
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    input = file.read()

    do = True

    dos = [do for do in re.finditer(do_pattern, input)]
    donts = [dont for dont in re.finditer(dont_pattern, input)]
    muls = [mul for mul in re.finditer(pattern, input)]
    truemuls = []
    nums = []

    # print(dos)
    # print(donts)

    results = 0

    for mul in muls:
        max = mul.span()[0]
        do_current = 0
        dont_current = 0

        for do in dos:
            if do.span()[0] > do_current and not do.span()[0] >= max:
                do_current = do.span()[0]
            # print(mul, do_current)
        for dont in donts:
            if dont.span()[0] > dont_current and not dont.span()[0] >= max:
                dont_current = dont.span()[0]
            # print(dont_current)

        if do_current > dont_current:
            do = True
        elif dont_current > do_current:
            do = False

        if do:
            truemuls.append(mul.group()[4:len(mul.group())-1])


    for mul in truemuls:
        nums.append(mul.split(','))
    
    for mul in nums:
        results += int(mul[0]) * int(mul[1])

    print(results)
