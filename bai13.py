'''
Viết chương trình đọc một số nguyên dương n từ người dùng và sau đó hiển thị tổng của tất cả các số 
nguyên từ 1 đến n. 
Tổng của n số nguyên dương đầu tiên có thể được tính bằng công thức: s = (n * n + 1)/2
'''
if __name__ == "__main__":
    n = int(input())
    s = (n * (n + 1)) / 2
    print(s)