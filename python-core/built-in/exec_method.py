"""
    Built-in Functions
"""

"""
    exec(): Thực thi code python dạng string
"""
# Mã nguồn cần thực thi
source_code = """
for i in range(5):
    print(i)
"""

# Sử dụng hàm exec() để thực thi mã nguồn
exec(source_code)
