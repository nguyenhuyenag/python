import traceback

try:
    pass
except ZeroDivisionError as e:
    print("Exception:", str(e))
    traceback.print_exc(limit=1)
else:
    pass
finally:
    pass
