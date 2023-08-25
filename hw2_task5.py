def sum_items(arr, max_num_sum):
    sp_new = []
    sum = 0
    sub_sp = []

    for i in range(len(sp)):
        if sum + sp[i] <= max_num_sum:
            sum += sp[i]
            sub_sp.append(sp[i])
        elif sp[i] <= max_num_sum:
            sum = sp[i]
            sp_new.append(sub_sp)
            sub_sp = []
            sub_sp.append(sp[i])

            if i + 1 == len(sp):
                sp_new.append(sub_sp)
        else:
            sum = 0
            sp_new.append(sub_sp)
            sub_sp = []
    print(sp_new)

sp = [0, 1, 5, 5, 2, 6, 2, 7]
x = 7

sum_items(sp, x)