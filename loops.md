# Loops
Loops are a fundamental concept in programming that allow you to repeatedly execute a block of code. They are used when you need to perform a specific task or a set of tasks multiple times without writing the same code over and over. In Python, there are mainly two types of loops: for loops and while loops. Additionally, there are loop control statements like break and continue that help control the flow of loops.

For Loop:
A for loop is used when you know how many times you want to execute a block of code. It iterates over a sequence (such as a list, tuple, string, or range) and performs an action for each item in the sequence.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

apple
banana
cherry

Example 2: Using a for loop with the range() function:

for i in range(1, 5):  # Iterates from 1 to 4
    print(i)

1
2
3
4

While Loop:
A while loop is used when you want to repeatedly execute a block of code as long as a certain condition is true.

count = 1
while count <= 5:
    print(count)
    count += 1

1
2
3
4
5

Loop Control Statements:
break Statement:
The break statement is used to exit a loop prematurely, even if the loop condition is still true. It's often used when a certain condition is met, and you want to terminate the loop immediately.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

apple

The continue statement is used to skip the current iteration of a loop and move to the next one. It's useful when you want to bypass certain items or conditions but continue the loop.

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

1
3
5

In summary, loops, including for and while loops, are essential for repetitive tasks in programming. You can control the flow of loops using break to exit prematurely and continue to skip the current iteration and move to the next one. These constructs make your code more flexible and powerful for various tasks.
