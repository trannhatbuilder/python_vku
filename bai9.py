import math
if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    A = float(input())
    B = float(input())
    C = float(input())

    s1 = 0.5 * a * b * math.sin(math.radians(C))
    s2 = 0.5 * a * c * math.sin(math.radians(B))
    s3 = 0.5 * b * c * math.sin(math.radians(A))

    s = a ** 2 * (math.sqrt(3)/4)

    print(s1, s2, s3, s, sep = " ")

    # đánh giá: các giá trị bằng nhau mặc dù sử dụng 2 công thức toán học khác nhau 
    
