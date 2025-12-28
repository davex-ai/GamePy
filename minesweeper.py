# position = input("Where would you like to dig? Input row, col: ").split(",")
# row = position[0]
# column = position[1]
# print(row, column)

def print_table():
    print("-" * 30)
    for _  in range(10):
        print("".join(str(_)))

print_table()