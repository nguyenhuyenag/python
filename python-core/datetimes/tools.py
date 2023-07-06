import calendar

nam = 2023
list_input = []
for i in range(1, 12 + 1):
    thang = str(i).zfill(2)
    # th_ = soT
    tu_ngay = f"{nam}-{thang}-01 00:00:00"
    print(calendar._monthlen(2023, i))
    ngay_cuoi_thang = calendar.monthrange(int(nam), int(i))[1]
    den_ngay = f"{nam}-{thang}-{ngay_cuoi_thang} 23:59:59"
    search_input = {'tu_ngay': tu_ngay, 'den_ngay': den_ngay}
    list_input.append(search_input)

print(list_input)