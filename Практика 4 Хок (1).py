salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
k = float
list = []
list1 = []
l = str
r = 0
print("Salary table:")
for i in  salary_list:
    list1 = []
    list = []
    k = i/100
    l = k*30
    l = round(l,2)
    list1.append(l)
    i += k*30
    i = round(i,2)
    list.append(i)
    print(salary_list[r], list[0], list1[0])
    r += 1