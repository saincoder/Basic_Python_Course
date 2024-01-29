import datetime

data_time = datetime.datetime.now()
print(data_time)

# print year
year = data_time.strftime("%Y")
print(f"Year: {year}")

# short form year
year = data_time.strftime("%y")
print(f"Year: {year}")

# print month
month = data_time.strftime("%b")
print(f"month: {month}")

month = data_time.strftime("%B")
print(f"month: {month}")

month = data_time.strftime("%m")
print(f"month: {month}")