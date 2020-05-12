import random

def main():
    #we set up a list of items
    names = ['Julie', 'Mehran', 'Simba', 'Ayesha', 'Karel']

    #.append is used to add an item to the end of a list
    names.append('Omar')

    #we use a for loop to iterate through the list and print out individual members of the list
    for name in names:
        print(name)

    #len is used to get the length of a list
    #i.e number of items in the list
    length_of_list = len(names)

    #index of a list starts its count from 0
    max_index = length_of_list - 1

    #f formats are used to print out strings
    #te=he value in brace brakets can be any data type
    print(f' the list has {length_of_list} items')
    print(f'the list has a maximum index of {max_index}')

    #we set the variable name 'index' to a random value provided the value is a valid index
    index = random.randint(0,max_index)

    #item_index prints the item at the random index above
    item_index = names[index]
    print(f'a random index is {index}')
    print(f'an item at a randomly selected index is {item_index}')

    #who is in what index
    print(names)
    prompt = input(f'Who is at index {index}?:  ')
    correct_answer = names[index]

    #it is possible to assign two or more variable names to two or more values
    #the .lower is used to set the values of prompt and correct_answer to lowercase to ensure that
    #no matter the format the user enters the values, the interpreter converts it to lowercase
    prompt , correct_answer = prompt.lower() , correct_answer.lower()
    if prompt == correct_answer:
        print('Correct!')
    else:
        print(f'Correct answer is, {correct_answer}')
if __name__ == '__main__':
    main()