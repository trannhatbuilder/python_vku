'''
Viết chương trình đọc chiều dài và chiều rộng của một cánh đồng từ người dùng. 
Hiển thị diện tích của cánh đồng theo theo đơn vị tính là Mẫu Anh. 
Gợi ý: Một Mẫu Anh bằng 43.560 met vuông.
'''
if __name__ == "__main__":
    length = float(input())
    width = float(input())
    area = (length * width) / 43560
    print(f"Area: {area:.4f}")
