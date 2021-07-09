li = ['appu', 'priya','heloooo','hell']
with open("a.txt") as f:
    a = f.read()

for i in li:
    s = a.replace(i, "***")

    with open("a.txt", 'w') as f:
        f.write(s)
