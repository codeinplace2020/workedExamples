def main():
    while True:
        # input function return string
        year_str = input('Please, input a year: ')

        # casting provided input into number
        year = int(year_str)

		# checking whether the provided year is evenly divisibly by 4
        if year % 4 == 0:
			# checking whether the provided year is evenly divisibly by 100
            if year % 100 == 0:
				# checking whether the provided year is evenly divisibly by 400
                if year % 400 == 0:
                    print('A given year {} is a leap year'.format(year))
                else:
                    print('A given year {} is NOT a leap year'.format(year))
            else:
                print('A given year {} is a leap year'.format(year))
        else:
            print('A given year {} is NOT a leap year'.format(year))
		
		# just printing dashes in order to seperate results in the console
        print('--------------------')


if __name__ == "__main__":
    main()
