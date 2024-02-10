import random

def guess(num):
    while True:
        try:
            return int(input(num))
        except ValueError:
            print("Incorrect Input!")
            
            
def calculate(a, operator, b):
    if operator == "+": 
        return a+b
    elif operator == "-": 
        return a-b
    elif operator == "*": 
        return a*b
    elif operator == "/": 
        return a//b 
    else: raise ValueError("Unsupported math operation")
    
    
totalQuestions = 10

correctAwnsers = 0
correctList = []
numbers = range(1,11)

for i in range(totalQuestions):
    operator = random.choice("+-*/")
    a, b = random.choice(numbers), random.choice(numbers)
    
    while operator == "/" and (a%b != 0 or a<=b):
        a, b = random.choice(numbers), random.choice(numbers)

    while operator == "-" and a<b:
        a, b = random.choice(numbers), random.choice(numbers)
        
    result = guess(f"What is {a} {operator} {b} = ")
    correct = calculate(a, operator, b)
    
    if result == correct:
        correctAwnsers += 1
        correctList.append((f"{a} {operator} {b}", True))
        print("Correct!\n")
    else:
        correctList.append((f"{a} {operator} {b}", False))
        print(f"Wrong. Correct solution is: {a} {operator} {b} = {correct}")
        
print(f"You got {correctAwnsers} out of {totalQuestions} questions correct.")

print("\nList of what you got right and wrong: ")
for question in correctList:
    if question[1]:
        print(f"{question[0]}     | Correct")
    else:
        print(f"{question[0]}     | Wrong")