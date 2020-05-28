import re
lines = ["surname: Obama, prename: Barack, profession: president", "surname: Merkel, prename: Angela, profession: chancellor"]
for line in lines:
    print(re.split(",* *\w*: ", line)[1:])
    
str = "yes I said yes I will Yes."
res = re.sub("[yY]es","no", str)
print(res)

