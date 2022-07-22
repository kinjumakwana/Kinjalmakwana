from re import S, X


def sum_num(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

inp = input('Enter your numbers(seperate by comma): ')
s=inp.split(',')
for n in s:
    if n.isnumeric():
        # for j in range(len(s)):
        a=sum_num(int(n))
print(a)
