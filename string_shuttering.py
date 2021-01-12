def multiply_table(num):
    tbl = []
    for c  in range(10):
        print(str(num) + " * " + str(c) + " = "+str(num*c))
        tbl.append(num*c)
        print(tbl)

multiply_table(9)

name = "KANNAN"
print(name.casefold())
print(name.count('N'))

