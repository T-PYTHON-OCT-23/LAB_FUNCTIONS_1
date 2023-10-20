def number(num: int):
    output = ""
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
              output += f"{j} "
        output += "\n"
    return output
       

pattern = number(7)
print(pattern)
