"""
    Thứ tự ưu tiên của các phép toán
        **
            * / % //
                + –
                    <= < > >=
                        <> == !=
                            = %= /= //= -= += *= **=
                                is , is not
                                    not, or, and
"""
x, y = 9, 4
print(f"Lũy thừa:       {x} ^ {y} = {x ** y}")
print(f"Chia thường:    {x} / {y} = {x / y}")
print(f"Chia nguyên:    {x} // {y} = {x // y}")
print(f"Chia dư:        {x} % {y} = {x % y}")

# x += 5
# print(x)
