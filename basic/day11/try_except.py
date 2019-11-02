while True:
    try:
        a = int(input("Nhap: "))
        break
    except ValueError:
        print("Vui long nhap so nguyen!")

print(a)
