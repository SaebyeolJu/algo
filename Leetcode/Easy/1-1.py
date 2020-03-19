def twosum(List,target):
    wait_list = set()
    finish_list = set()

    for num in List:
        need_num = target - num
        if(need_num not in wait_list):
            wait_list.add(num)
        else:
            finish_list.add((min(need_num, num), max(need_num, num)))

    print('\n'.join(map(str, list(finish_list))))
twosum([2,7,1,3,6,8],9)