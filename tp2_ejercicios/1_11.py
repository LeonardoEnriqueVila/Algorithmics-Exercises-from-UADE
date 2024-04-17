# 1 m = 60 s
# 1 h = 3600 s
# 1 d = 86400 s

seconds = int(input("Get Seconds: "))
initialSeconds = seconds
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{initialSeconds} seconds are {days} days, {hours} hour, {minutes} minutes, and {seconds} seconds")
