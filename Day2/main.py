def is_safe(list:list, dampener:bool=False) -> bool:
    '''
    Takes list input and returns whether or not the list is a safe report
    '''
    if dampener and not is_safe(list):
        return problem_dampener(list)

    if only_ascending(list) ^ only_descending(list):
        for i in range(len(list)-1):
            if abs(int(list[i]) - int(list[i+1])) > 3 or abs(int(list[i]) - int(list[i+1])) < 1:
                return False
    else:
        return False

    return True

def only_ascending(list: list) -> bool:
    for i in range(len(list)-1):
        if int(list[i]) > int(list[i+1]):
            return False
    return True

def only_descending(list: list) -> bool:
    for i in range(len(list)-1):
        if int(list[i]) < int(list[i+1]):
            return False
    return True

def problem_dampener(list: list):
    for i in range(len(list)):
        new_list = list.copy()
        new_list.pop(i)

        if is_safe(new_list):
            return True
    return False



with open('input.txt', 'r') as file:
    safe_reports = 0
    safe_with_damp = 0
    for line in file:
        list = line.split()
        if is_safe(list):
            safe_reports += 1
        if is_safe(list, dampener=True):
            safe_with_damp += 1
    
    print(f'Safe reports: {safe_reports}')
    print(f'Safe reports with dampener: {safe_with_damp}')
