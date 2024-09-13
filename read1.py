author = input("Хто написав?")

with open(
"file.txt", 'a', encoding = "utf-8" 
) as file:
    file.write(f"({author})\n")
with open(
"file.txt", 'r', encoding = "utf-8" 
) as file:
    for line in file:
        print(line)