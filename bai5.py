'''
nhap vao 1 chuoi
5 ky tu cuoi cung, 5 ky tu dau tien
4 chuoi tren mot dong cach 1 khoang trang
4 chuoi tren 4 dong
'''
st = input()
first_five_chrac = st[:5]
last_five_chrac = st[len(st)-5:]
four_str_1_line = 4 * (st + " ")
four_str_4_line = 4 * (st + "\n")

print(first_five_chrac)
print(last_five_chrac)
print(four_str_1_line)
print(four_str_4_line)