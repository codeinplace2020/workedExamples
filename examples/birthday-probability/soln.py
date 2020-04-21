'''
what is the probability that two people in a group share the same birthday?
prompt the user to enter the number of people in a group
compute the probability that at least two people in the group share the same birthday
'''

# constant: days in the year, change this to 366 for leap years
DAYS_IN_YEAR = 365

def main():
    # ask the user for the number of people in a group
    # the user should enter a number, but python will put it in a string-type variable
    people_in_group_str = input('How many people are in the group? ')

    # convert the string-type variable to an integer
    people_in_group = int(people_in_group_str)
    
    # validate the user's input since it takes at least 2 people to make a group
    if people_in_group < 2:
        print('You need at least two people to make a group!')
        return

    # compute the numerator of the probability equation
    prob_numerator = 1.0
    for i in range(people_in_group):
        prob_numerator = prob_numerator * (DAYS_IN_YEAR - i)
    
    # compute the denominator of the probability equation
    prob_denominator = 365 ** people_in_group

    # calculate the probability that nobody shares a birthday
    prob_nobody = prob_numerator / prob_denominator

    # calculate probability that at least two people share a birthday
    prob_somebody = 1 - prob_nobody

    # convert the probability to a percentage with at most two digits after the decimal
    prob_somebody_pct = round(prob_somebody * 100, 2)

    # convert the probability percentage to a string that we can display to the user
    prob_somebody_pct_str = str(prob_somebody_pct)

    # display the result to the user
    response = 'There is a ' + prob_somebody_pct_str + '% chance '
    response = response + 'at least two people share the same birthday!'
    print(response)

if __name__ == '__main__':
	main()
