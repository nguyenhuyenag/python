import re

line = "cong hoa xa hoi chu nghia viet nam doc lap tu do h"

matchObj=re.match(r'(.*) viet (.*?) .*',line,re.M|re.I)

if matchObj :
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
    print("matchObj.group(): ", matchObj.group())
else:
    print("No match!!!")
    

