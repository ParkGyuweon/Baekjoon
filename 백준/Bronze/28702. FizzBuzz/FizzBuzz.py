commands = []
for i in range(3):
    commands.append(input())
number = 0
if commands[0].isnumeric():
    number = int(commands[0]) + 3
elif commands[1].isnumeric():
    number = int(commands[1]) + 2
elif commands[2].isnumeric():
    number = int(commands[2]) + 1

if number % 15 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)