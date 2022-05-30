def flip(word):
	flippedword = ''
	for i in range(len(word)-1, -1, -1):
		flippedword += (word[i])
	return flippedword
	
		

def checkpalindrome():
	word = ""
	print("A palindrome is a word or sequence that reads the same backward and forward.")
	print("This can check if any word is a palindrone. Try it.")
	print("Type the word you would like to check below.")
	word = input()
	flipped = flip(word)
	if flipped == word:
		print("yes")
	else:
		print("no")
		
checkpalindrome()

