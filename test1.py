n = int(input("enter number N: " ))
str_a = input(f"input difficulties for {n} tasks: ")
try:
    list_b = str_a.split(" ")
    list_b = [int(x) for x in list_b]
except Exception:
    print("-1")
    exit("1")
if n != len(list_b) or n % 2 == 1:
    print("-1")
    exit(1)

list_sorted = sorted(list_b)

difficulty = int
diff_equal = True
# split to pairs:
for i in range(int(n/2)):
    # print(f" pair {list_sorted[i]}  {list_sorted[n - 1 - i]}")
    difficulty = list_sorted[i] + list_sorted[n - 1 - i]
    if i == 0:
        difficulty_0 = difficulty
        continue
    else:
        if difficulty == difficulty_0:
            continue
        else:
            print("-1")
            exit("-1")

print(difficulty_0)





