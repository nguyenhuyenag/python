s = "-abc+3a+2ac"

result = []
current_term = ""
for char in s:
    if char in "+-" and current_term:
        result.append(current_term)
        current_term = char
    else:
        current_term += char

# Thêm phần tử cuối cùng vào kết quả
if current_term:
    result.append(current_term)

# Loại bỏ dấu "+" ở đầu các thành phần không mang ý nghĩa
result_array = [term[1:] if term.startswith('+') else term for term in result]

print(result_array)
