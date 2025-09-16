# cho chuoi bieu dien dia chi email
# rut trich va hien thi chuoi "gmail.com"
data = ' nhattn.22ns@vku.udn.vn'
position = data.find("@")
host = data[position + 1:]
print(host)