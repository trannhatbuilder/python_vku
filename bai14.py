'''
Viết một chương trình đọc hai số nguyên a và b từ người dùng. Chương trình sẽ tính toán và hiển thị:
Tổng của a và b
Hiệu của a và b
Tích của a và b
Thương của a chia cho b
Phần còn lại khi a được chia cho b
Kết quả của log10_a
Kết quả của a^b
'''
import math
if __name__ == "__main__":
    a = float(input())
    b = float(input())

    sum = a + b
    subtract = a - b
    product = a * b
    quotient = a / b
    remainder = a % b
    log10_a = math.log10(a)
    power = a ** b

    print(sum, subtract, product, quotient, remainder, log10_a, power, sep = "\n")
