def is_punctuation(char):
	return char in ('.', '?', '!')

def is_vowel(char):
	return char.lower() in ('a', 'e', 'i', 'o', 'u')

def is_consonant(char):
	return not is_vowel(char)

def main():
	print('This program translates words/phrases from English to Pig Latin. To end the program, type EXIT.')
	
	# initially asks for a word/phrase to translate before entering while loop
	in_str = input('Word/phrase to translate: ')
	out_str_list = []
	out_str = ''

	# while the input string from the user is not 'EXIT', translate the input string in English to Pig Latin
	while in_str != 'EXIT':
		# splits the input into a list of strings, each element is one word
		in_str_list = in_str.split()

		# translates each word in the list of English words to Pig Latin
		for word in in_str_list:
			# initializes the pl_word to just hold the original word
			# the rest of the code works on altering pl_word according to the translation rules
			pl_word = word
			punctuation = ''

			# checks that word is at least 1 letter long
			if len(word) >= 1:
				# if the last character of the word is punctuation, strips it off before translating the rest of the word
				# and adds it back at the end of the word later
				if is_punctuation(word[-1]):
					pl_word = word[0:-1]
					punctuation = word[-1]

				# translates the word based on Pig Latin translation rules
				if is_vowel(word[0]):
					pl_word = pl_word.lower() + 'yay'
				if is_consonant(word[0]):
					first_vowel_index = 0
					while first_vowel_index < len(word) and not is_vowel(word[first_vowel_index]):
						first_vowel_index += 1
					pl_word = pl_word.lower()[first_vowel_index:] + pl_word.lower()[0: first_vowel_index] + 'ay'
				
				# preserves case by capitalizing the first letter of the translated word if
				# the first letter of the original word was capitalized
				if word[0].isupper():
					pl_word = pl_word.capitalize()

			# adds punctuation back onto the translated word
			pl_word = pl_word + punctuation

			# adds the translated word to a list of translated words
			out_str_list.append(pl_word)

		# joins all the words in the list of translated words, with a ' ' (space character) between each word 
		# to form the whole translated word/phrase
		out_str = ' '.join(out_str_list)

		# prints out the whole translated word/phrase
		print(out_str)

		# asks for another word/phrase to translate in the while loop
		in_str = input('Word/phrase to translate: ')
		out_str_list = []
		out_str = ''

if __name__ == '__main__':
	main()