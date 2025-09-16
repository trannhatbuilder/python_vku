'''
Viết chương trình yêu cầu người dùng nhập chiều rộng và chiều dài của một căn phòng. 
Chiều dài và chiều rộng sẽ hiển thị kiểu số dấu phẩy động. Hiển thị diện tích căn phòng. 
'''
if __name__ == "__main__":
    a = float(input())
    b = float(input())
    s = a * b
    print(f"length: {a:.2f}")
    print(f"width: {b:.2f}")
    print(f"area: {s:.2f}")