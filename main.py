def calculateNumbers(num1, num2):
    return num1 + num2


x = 10
y = 12
z = calculateNumbers(x, y)
print(f"{x} + {y} = {z}")

number = 123456789
string = str(number)
print(f"length : {len(string)}")

num = [2, 6, 4, 5, 1]
print(num)
num.append(10)
print(num)
num.sort()
print(num)
print(len(num))

item = ["one", "two", "three", "four"]
print(item)
item.append("five")
print(item)
item.sort()
print(f"sorted item : {item}")

num1 = int(input("প্রথম নাম্বারটি দিন : "))
num2 = int(input(" দ্বিতীয় নাম্বারটি দিন : "))


def greaterNumPrint(x):
    print(f"larger number is {x}")


if num1 > num2:
    greaterNumPrint(num1)
elif num1 == num2:
    greaterNumPrint(num1)
else:
    greaterNumPrint(num2)

if num1 % 2 == 0 or num2 % 2 == 0:
    print("one number is even")
elif num1 % 2 == 0 and num2 % 2 == 0:
    print("numbers are even")
else:
    print("numbers are বিজোড়")

print(num1 % 2, num1 / 2, num1 // 2)  # % modulus operator, / division operator, // quotient(ভাগফল) operator


def checkEvenNum(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_nums = list()

count = 0;

for i in range(0, 101):
    if checkEvenNum(i):
        even_nums.append(i)
        count = count+1


print(even_nums)
print(count)

item = list(map(int, input("Enter the array : ").split()))

# for i in range(0, 5):
#     x = int(input())
#     item.append(x)

print(item)
item.sort()
print(item)
