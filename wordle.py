
## Functions -------------------------------------------------

def main():
    """Main function"""
    words = import_all_words(filename)
    answer = get_answer(words)
    guess = "" 
    counter = 0
    while True:
        guess = input("Enter your guess\n").lower()
        if not valid_input(guess, words):
            pass
        elif answer == guess:
            print(f"{answer} is the correct answer!")
            print(f"Result: {counter} tries")
            return 0
        else:
            counter += 1 
            prompt = generate_prompt(answer, guess)
            print(prompt)
    return 1 

def import_all_words(filename):
    """Import all 5 letter words from specific file"""
    words = set()
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            words.add(line.strip())
    return words

def get_answer(words):
    """"Get a random word form list of all words"""
    answer = words.pop().lower()
    words.add(answer)
    return answer
    
def valid_input(guess, words):
    """Check if the guess is valid according to wordle rule"""
    if len(guess) != 5:
        print("Enter exactly 5 characters")
        return False
    elif not guess.isalpha():
        print("Enter only alphabets")
        return False
    elif not guess in words:
        print("Not a valid word")
        return False
    return True

def generate_prompt(answer, guess):
    """Check the valid guess against the answer and return appropriate prompts"""
    answer_list, guess_list = list(answer), list(guess)
    green_list, yellow_list = [], []
    for i in range(5):
        if guess[i] == answer[i]:
            green_list.append(guess[i])
        elif guess[i] in answer:
            yellow_list.append(guess[i])
    prompt = f"Green:{green_list} " +\
             f"Yellow:{yellow_list}"   
    return prompt


## Variables -------------------------------------------------

filename = "fiveletters.txt"

## Execution -------------------------------------------------

if __name__ == "__main__":
    main()
