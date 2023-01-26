s = list(input().split())
num_1 = int(s[0])
num_2 = int(s[2])
if s[1] == "+":
    print(num_1 + num_2)
elif s[1] == "-":
    print(num_1 - num_2)
elif s[1] == "*":
    print(num_1 * num_2)
elif s[1] == "/":
    print(num_1 / num_2)
else:
    print("Unknown command")