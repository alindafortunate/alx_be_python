# pattern_drawing.py
pattern = int(input("Enter the size of the pattern: "))
size = 0
while size < pattern:
    for x in range(pattern):
        print("*", end="")
    print("")
    size += 1
