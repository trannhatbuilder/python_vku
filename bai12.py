'''
Viết chương trình nhập chi phí của một bữa ăn tại nhà hàng từ người dùng.
Chương trình sẽ tính thuế và tiền boa cho bữa ăn. 
Trong đó, tiền boa là 18% số tiền bữa ăn (không có thuế); tiền thuế là 5% số tiền bữa ăn. 
Đầu ra của chương trình là tổng tiền, gồm: thuế, số tiền boa và tiền bữa ăn. 
Định dạng đầu ra sao cho tất cả các giá trị được hiển thị bằng hai con số thập phân
'''
if __name__ == "__main__":
    n = float(input())
    tax = n * 0.05
    boa = n * 0.18
    total = tax + boa + n
    print(f"Total: {total:.2f}")