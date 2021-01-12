def is_curzon(num):
    #chk_cur = ((num**5)+1)/((num*5)+1)
    chk_cur = ((2 ** num) + 1) % ((2 * num) + 1)
    if chk_cur==0:
        return "It's a curzon number"
    else:
        return "It's not a curzon number"



print(is_curzon(5))
print(is_curzon(10))