f = open('workfile', 'w', encoding="utf-8")
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
f.closed
print(f.closed)
f.close()
f.read()
