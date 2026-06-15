# Simple Quiz Game in Python

score = 0

print("Welcome to Python Quiz Game!")
print()

# Question 1
answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()

# Question 2
answer = input("2. Which language is used for AI mostly? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()

# Question 3
answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()
# Question 4
answer = input("What is the correct spelling of pyton?")
if answer.lower() == "python"
    print("Correct!")
    score +=1
esle:
    print("Wrong")
# Question 5
answer = input("How many months in a year?")
if answer.lower() == "12"
    print("Correct!")
    score +=1
esle:
    print("Wrong")

# Final Score
print("Quiz Finished!")
print("Your score is:", score, "/ 5")
