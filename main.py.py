import random
import time

numb=0
def inp_number():      
    print("Use IDE like Visual Studio and practice this question")
    print("You can also insert any number to check its choosen type number")
    numb=int(input("Enter A Number: "))
    return numb

def outp():
    print("BTW did your answer come (Enter Y/N)")  
    ch = input()[0]
    if ch == 'Y' or ch == 'y':
        print("Good You Are Going Good")
    else:
        print("No Worries You Should Try Again ")
        # ask if user wants to play guessing game
        play = input("Do you want to play a Number Guessing Game to refresh? (Y/N): ")
        if play.lower() == 'y':
            number_guessing_game()

def even_number():
    print("In this program you have to check whether a given number is even or odd")
    print("For example, if user enters 3 → Output: Odd Number")
    print("Whereas if user enters 2 → Output: Even Number")
    
    numb=inp_number()
    if(numb%2==0):
          print("Even Number")
    else:
          print("Odd Number")   

    outp() 

count=0
def prime_number():
    print("In this program you have to check the factors of that number.")
    print("If it is only divisible by 1 and itself, then it’s a prime number.")
    print("Example: 7 is Prime, 4 is Not Prime")
    print()

    numb = inp_number()
    count = 0            

    for i in range(1, numb + 1):  
        if numb % i == 0:
            count += 1

    if count == 2:  
        print("Prime Number")
    else:
        print("Not a Prime Number")

    outp()

def palindrome_number():
     print("Number is said to be a Palindrome Number if Reverse of Same Number is Equal to Number itself")
     print("Suppose 121 when reversed gives same number 121 so it is a Palindrome Number")
     numb=inp_number()
     rev=0
     temp=numb
     while numb > 0:
          rev = rev * 10 + (numb % 10)
          numb//=10
     if(rev == temp):
          print("Entered Number is Palindrome")
     else:
          print("Entered Number is not a Palindrome Number")

     outp()

def armstrong_number():
    print("A number is Armstrong if the sum of its digits raised to the power of number of digits equals the number itself.")
    print("Example: 153 → Armstrong (1³+5³+3³=153)")
    print("Example: 123 → Not Armstrong (1³+2³+3³=36)")
    numb=inp_number()
    digit=len(str(numb)) 
    total=0
    temp=numb
    while(numb>0):
         total+=(numb%10) ** digit
         numb//=10
    if(total == temp):
         print("Entereed Number is Armstrong Number")
    else:
         print("Entered Number is not Amstrong Number")
    outp()

def spy_number():
     
    print("A Spy Number is a number where sum of digits equals product of digits.")
    print("Example: 1124 → (1+1+2+4=8, 1×1×2×4=8) → Spy Number")

    numb = inp_number()
    s = 0  
    p = 1  
    temp = numb

    while numb > 0:
        d = numb % 10
        s += d
        p *= d
        numb //= 10

    if s == p:
        print(temp, "is a Spy Number")
    else:
        print(temp, "is NOT a Spy Number")

    outp()

def neon_number():
     
    print("A Neon Number is a number where sum of digits of square of number equals the number itself.")
    print("Example: 9 → 9²=81 → 8+1=9 → Neon Number ")

    numb = inp_number()
    sq = numb * numb
    s = 0
    temp = sq

    while sq > 0:
        s += sq % 10
        sq //= 10

    if s == numb:
        print(numb, "is a Neon Number")
    else:
        print(numb, "is NOT a Neon Number")

    outp()

def automorphic_number():
    print("An Automorphic Number is a number whose square ends with the same number.")
    print("Example: 25 → 25²=625 → ends with 25 → Automorphic ")

    numb = inp_number()
    sq = numb * numb

    if str(sq).endswith(str(numb)):
        print(numb, "is an Automorphic Number")
    else:
        print(numb, "is NOT an Automorphic Number")

    outp()

def special_number():
    print("A Special Number is a number where sum of factorials of digits equals the number itself.")
    print("Example: 145 → 1!+4!+5! = 145 → Special Number")

    numb = inp_number()
    temp = numb
    total = 0

    while numb > 0:
        d = numb % 10
        fact = 1
        for i in range(1, d+1):
            fact *= i
        total += fact
        numb //= 10

    if total == temp:
        print(temp, "is a Special Number")
    else:
        print(temp, "is NOT a Special Number")

    outp()

def perfect_number():
    print("A Perfect Number is a number where the sum of its proper divisors equals the number itself.")
    print("Example: 28 → 1+2+4+7+14=28 → Perfect Number")

    numb = inp_number()
    s = 0

    for i in range(1, numb):
        if numb % i == 0:
            s += i

    if s == numb:
        print(numb, "is a Perfect Number")
    else:
        print(numb, "is NOT a Perfect Number")

    outp()


def strong_number():
    print("A Strong Number is a number where the sum of factorials of digits equals the number itself.")
    print("Example: 145 → 1!+4!+5! = 145 → Strong Number")

    numb = inp_number()
    temp = numb
    total = 0

    while numb > 0:
        d = numb % 10
        fact = 1
        for i in range(1, d+1):
            fact *= i
        total += fact
        numb //= 10

    if total == temp:
        print(temp, "is a Strong Number")
    else:
        print(temp, "is NOT a Strong Number")

    outp()


def harshad_number():
    print("A Harshad (Niven) Number is divisible by the sum of its digits.")
    print("Example: 18 → 1+8=9 → 18 is divisible by 9 → Harshad Number")

    numb = inp_number()
    s = 0
    temp = numb

    while numb > 0:
        s += numb % 10
        numb //= 10

    if temp % s == 0:
        print(temp, "is a Harshad Number")
    else:
        print(temp, "is NOT a Harshad Number")

    outp()


def fibonacci_series():
    print("Fibonacci Series is a sequence where each number is sum of previous two numbers.")
    print("Example: 0, 1, 1, 2, 3, 5, 8, ...")

    terms = int(input("Enter how many terms you want in Fibonacci Series: "))
    a, b = 0, 1

    print("Fibonacci Series:")
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a+b
    print()


def reverse_number():
    print("This program will reverse the digits of a number.")
    print("Example: 1234 → 4321")

    numb = inp_number()
    rev = 0
    temp = numb

    while numb > 0:
        rev = rev * 10 + (numb % 10)
        numb //= 10

    print("Reverse of", temp, "is", rev)
    outp()


score = 0
POINTS_CORRECT = 10
POINTS_WRONG = -10
POINTS_QUIZ_CORRECT = 15

HINTS = {
    1: "Even: check numb % 2 == 0.",
    2: "Prime: a prime has exactly two divisors: 1 and itself.",
    3: "Palindrome: reverse digits and compare to original.",
    4: "Armstrong: sum of each digit^count_of_digits equals number.",
    5: "Spy: sum of digits equals product of digits.",
    6: "Neon: sum of digits of square equals the number.",
    7: "Automorphic: square ends with the number itself.",
    8: "Special/Strong: usually sum of factorials of digits equals number.",
    9: "Perfect: sum of proper divisors equals the number.",
    10: "Strong: (same as special in your code) factorial-sum check.",
    11: "Harshad: number divisible by sum of its digits.",
    12: "Fibonacci: sequence where each term is sum of previous two.",
    13: "Reverse: produce digits in reverse order."
}


NOTES = {
    1: "Did you know? 0 is even. Even numbers are divisible by 2.",
    2: "Did you know? 2 is the only even prime.",
    3: "Did you know? Palindromes can be numeric or textual.",
    4: "Did you know? 153, 370, 371 and 407 are 3-digit Armstrong numbers.",
    5: "Did you know? Spy numbers are less commonly used but good practice for digit ops.",
    6: "Did you know? 9 is a classic example of a Neon number.",
    7: "Did you know? 5, 6, 25, 76 are examples of automorphic numbers.",
    8: "Did you know? Special and Strong numbers are sometimes synonyms; check definitions.",
    9: "Did you know? 6 and 28 are the first two perfect numbers.",
    10: "Did you know? Strong numbers are rare; 145 is a classic example.",
    11: "Did you know? Harshad numbers are also called Niven numbers.",
    12: "Did you know? Fibonacci numbers appear in nature (flower petals, pine cones).",
    13: "Did you know? Reversing a number is useful in many digit-manipulation algorithms."
}


DIFFICULTY_BUCKETS = {
    'easy': [1, 3, 13],          
    'medium': [2, 4, 6],         
    'hard': [5, 7, 8, 9, 10, 11] 
}


MOTIVATIONS_RIGHT = [
    "Great job! You're on fire ",
    "Nice! Keep it up ",
    "Excellent — you're improving fast "
]   
MOTIVATIONS_WRONG = [
    "Don’t worry — mistakes are how we learn ",
    "Try again — you’ll get it next time!",
    "Keep practicing — you're doing fine!"
]


QUIZ_QUESTIONS = [
    {
        "q": "Which of the following is a prime number?",
        "options": ["9", "11", "15", "21"],
        "ans": "11"
    },
    {
        "q": "Which of the following is an Armstrong number?",
        "options": ["123", "153", "200", "3700"],
        "ans": "153"
    },
    {
        "q": "Which of the following is a Neon number?",
        "options": ["3", "9", "10", "12"],
        "ans": "9"
    },
    {
        "q": "Which number is Automorphic?",
        "options": ["10 (100)", "25 (625)", "12 (144)", "7 (49)"],
        "ans": "25 (625)"
    }
]

def number_guessing_game():
    print("\n🎲 Welcome to the Number Guessing Game! ")
    print("Try to guess a number between 1 and 10.")
    secret = random.randint(1, 10)
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input — returning to main menu.")
        return
    if guess == secret:
        print("🎉 Wow! You guessed it right!")
    else:
        print(f"Oops! The number was {secret}. Better luck next time!")
    print()


def quiz_mode():
    global score
    print("\n QUIZ MODE — Answer one multiple-choice question for bonus points.")
    q = random.choice(QUIZ_QUESTIONS)
    print("Q:", q["q"])
    for idx, opt in enumerate(q["options"], start=1):
        print(f" {idx}. {opt}")
    ans = input("Enter the answer (type the option text or number): ").strip()
    # normalize input
    chosen = ans
    if ans.isdigit():
        idx = int(ans) - 1
        if 0 <= idx < len(q["options"]):
            chosen = q["options"][idx]
    if chosen == q["ans"]:
        print("Correct! +", POINTS_QUIZ_CORRECT, "points")
        score += POINTS_QUIZ_CORRECT
    else:
        print("Incorrect. The right answer is:", q["ans"])
    print("Current score:", score)
    print()


def run_program_with_features(program_id):
    """
    Show hint, run the selected program (calls the original function),
    then ask the user to mark if they were correct for scoring.
    Show motivation and note, allow quiz/game options.
    """
    global score

    
    hint = HINTS.get(program_id, "")
    if hint:
        print("\n HINT:", hint)

    
    program_map = {
        1: even_number,
        2: prime_number,
        3: palindrome_number,
        4: armstrong_number,
        5: spy_number,
        6: neon_number,
        7: automorphic_number,
        8: special_number,
        9: perfect_number,
        10: strong_number,
        11: harshad_number,
        12: fibonacci_series,
        13: reverse_number
    }

    func = program_map.get(program_id)
    if not func:
        print("Program not implemented.")
        return

   
    func()

   
    while True:
        resp = input("Did you solve it correctly? (Y/N): ").strip().lower()
        if resp == 'y':
            score += POINTS_CORRECT
            print(random.choice(MOTIVATIONS_RIGHT))
            break
        elif resp == 'n':
            score += POINTS_WRONG
            print(random.choice(MOTIVATIONS_WRONG))            
            play = input("Do you want to play a quick Number Guessing Game to relax? (Y/N): ").strip().lower()
            if play == 'y':
                number_guessing_game()
            break
        else:
            print("Please enter Y or N.")
    note = NOTES.get(program_id)
    if note:
        print("\n📚 Note:", note)
    print("Your current score is:", score)
    print("-" * 50)
    qplay = input("Do you want to try a short quiz for bonus points? (Y/N): ").strip().lower()
    if qplay == 'y':
        quiz_mode()


def pick_from_difficulty(level):
    level = level.lower()
    bucket = DIFFICULTY_BUCKETS.get(level)
    if not bucket:
        
        return random.randint(1, 13)
    return random.choice(bucket)


def main():
    global score
    print("********* Welcome To Techhyy Learners *********")
    print("This Platform is especially for beginners and is beginner friendly.")
    print("Here you can practice number manipulation questions with explanations.\n")

    
    while True:
       
        mode = input("Do you want to choose a program yourself? (Y = choose / N = platform chooses): ").strip().lower()
        if mode == 'y':
            
            print("\nChoose a program:")
            print("1 Even  2 Prime  3 Palindrome  4 Armstrong  5 Spy  6 Neon  7 Automorphic")
            print("8 Special 9 Perfect 10 Strong 11 Harshad 12 Fibonacci 13 Reverse")
            try:
                choice = int(input("Enter program number (1-13): "))
                if not (1 <= choice <= 13):
                    print("Invalid selection; please choose between 1 and 13.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            
            print("\nChoose difficulty for platform to pick from: Easy / Medium / Hard")
            level = input("Enter difficulty (Easy/Medium/Hard) or press Enter for random: ").strip().lower()
            if level == '':
                
                choice = random.randint(1, 13)
            else:
                choice = pick_from_difficulty(level)
            print(f"Platform selected Program {choice} for you.\n")


        print("-" * 50)
        run_program_with_features(choice)

        cont = input("Do you want to try another program? (Y/N): ").strip().lower()
        if cont != 'y':
            print("\nFinal score:", score)
            if score >= 100:
                print("Amazing! You're doing excellent. Keep practicing 🚀")
            elif score >= 50:
                print("Great progress! Keep going 💪")
            else:
                print("Good effort — keep practicing and you'll improve fast!")
            print("Thanks for using Techhyy Learners.!")
            break

if __name__ == "__main__":
    main()