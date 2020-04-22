import random

NUM_QUESTIONS = 3


def main():
    welcome_message()
    # Initialize the names of three gods
    A, B, C = assign_names() 
    # User poses questions to the three gods
    for i in range(NUM_QUESTIONS):
        print(f'\n================== Question #{i+1} ==================')
        ask_one_question(A, B, C)
    # Getting asnwer from the user
    get_solution(A, B, C)


def welcome_message():
    print('Welcome! You are about to solve "The Hardest Logic Puzzle Ever"!')
    print('  There are 3 gods A, B, and C. Their names are, in no particular')
    print('  order, Truth, False, and Random. You can ask 3 yes/no questions')
    print('  and in the end, you need to tell the names of A, B, and C. One')
    print('  challenging part is that these gods speak another language, so')
    print('  they can only answer "da" or "ya". Unfortunately, you have no')
    print('  idea whether "da" means "yes" or "no".')
    print('-----------------------------------------------------------------')
    print('Hint: your question can be strategically structured in the')
    print('      following way:')
    print('   *************************************************************')
    print('   If I asked you "Is [God] named [Name]?", would you say [Ans]?')
    print('   *************************************************************')
    print('      where [God] can be A, B, or C')
    print('           [Name] can be True, False, or Random')
    print('            [Ans] can be da or ya')
    print('-----------------------------------------------------------------')    


def ask_one_question(A, B, C):
    """
    User asks a selected god a carefully crafted question and 
    gets the asnwer from that god
    """
    # Select whom to ask and set up the question
    who = input('Who do you want to ask (enter A, B, or C)? ' )
    print('Your question is in the following format:')
    print('   If I asked you "Is [God] named [Name]?", would you say [Ans]?')
    god = input('Enter [God] (A, B, or C): ')
    name = input('Enter [Name] (True, False, or Random): ')
    ans = input('Enter [Ans] (da or ya): ')
    print(f'You asked {who}:')
    print(f'   If I asked you "Is {god} named {name}?", would you say {ans}?')
    
    # Obtain the answer from the selected god
    true_ans = check_name(god, name, A, B, C)
    ans_from_who = evaluate(who, true_ans, ans, A, B, C)
    print(f">>> {who}'s answer is {ans_from_who}.")


def get_solution(A, B, C):
    """
    Asks user for the solution to the puzzle. Reveals the correct answer
    if the user gets it wrong.
    """
    print('\n-------------------------------------------------------------\n')
    A_input = input("What is A's name? (enter True, False, or Random) ")
    B_input = input("What is B's name? (enter True, False, or Random) ")
    C_input = input("What is C's name? (enter True, False, or Random) ")
    if A_input == A and B_input == B and C_input == C:
        print('Congratulations! You nailed it!')
    else:
        print('Sorry, your answer is wrong. The correct answer is:')
        print(f'  A is "{A}", B is "{B}", and C is "{C}".')


def evaluate(who, true_ans, ans, A, B, C):
    """
    Evaluates the answer from the selected god
    Returns 'da' or 'ya'.
    It uses a key insight that asking either True or False the question:
    >>> If I asked you Q, would you say da?
    results in da if Q is indeed true and in ya if Q is false. It does not
    matter whether da means yes or no.
    """
    if check_name(who, 'Random', A, B, C):
        if random.random() < 0.5:
            return 'da'
        else:
            return 'ya'
    else:
        if true_ans:
            return ans
        else:
            return flip_da_ya(ans)


def flip_da_ya(ans):
    if ans == 'da':
        return 'ya'
    else:
        return 'da'


def check_name(god, name, A, B, C):
    """
    Evaluates whether a given god has a particular name.
    Returns True if the god has the given name, False otherwise
    """
    if god == 'A':
        return name == A
    elif god == 'B':
        return name == B
    else:
        return name == C


def assign_names():
    """
    Returns a randomly shuffled list of names for the three gods
    """
    names = ["True", "False", "Random"]   
    random.shuffle(names)
    return names


if __name__ == '__main__':
    main()
