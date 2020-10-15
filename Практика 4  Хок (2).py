s = list(input("Введіть текст:"))
l = 1
for j in s:
    if j == ',':
        l += 1
if l == 1:
    str1 = ''.join(s)
    print(str1)
else:
 print(l)
 c = 0
 k = 0
 for i in s:
     if i == ',':
        k += 1
     if  k == l - 1:
       s[c] = " and"
       break
     c += 1
 str1 = ''.join(s)
 print(str1)