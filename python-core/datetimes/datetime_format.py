from datetime import datetime

date_string = "03/19/2021"

date_object = datetime.strptime(date_string, "%m/%d/%Y")
formatted_date = date_object.strftime("%Y-%m-%d")

print(formatted_date)
