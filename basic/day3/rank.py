def checkRanking(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

t, l, h = eval(input("Toan = ")), eval(input("Ly = ")), eval(input("Hoa = "))

# avg = (t + l + h) / 3

# if t < 79 or l < 79 or h < 79:
#     avg -= 10

avg = t + l + h

if avg < 79 + 200:
    avg -= 10

avg = avg / 3

print("Xe hang: ", checkRanking(avg))
