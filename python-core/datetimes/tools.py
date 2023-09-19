import calendar

nam = 2023
list_input = []
for i in range(1, 12 + 1):
    thang = str(i).zfill(2)
    tu_ngay = f"{nam}-{thang}-01"

    # print(i, calendar._monthlen(nam, i))
    # print(calendar.monthrange(int(nam), int(i)))

    ngay_cuoi_thang = calendar.monthrange(int(nam), int(i))[1]
    den_ngay = f"{nam}-{thang}-{ngay_cuoi_thang}"
    search_input = {'tu_ngay': tu_ngay, 'den_ngay': den_ngay}
    list_input.append(search_input)

print(list_input)