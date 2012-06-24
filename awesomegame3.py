import random, operator, signal

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def raw_input_with_timeout(prompt='> ', timeout=5):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        answer = raw_input(prompt)
        signal.alarm(0)
        return answer
    except AlarmException:
        print '\nSorry, too slow.'
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def check_guess(guess):
	try:
		int(guess)
		return True
	except ValueError:
		return False

def check_for_challenged(guess):
	while check_guess(guess) == False:
		print "We all struggle sometimes. Just type in a regular old number to turn this setback into a comeback!"
		guess = raw_input("Guess now: ")
	return int(guess)

print "Welcome to my awesome game!"
name = raw_input("What is your name? ").strip().title()
print "Great, %r, let's get started having fun!" %name
# 
# number = random.randint(1,24)
# guess = raw_input("First, you must choose the best number between 1 and 24. Guess now: ").strip()
# 
# while guess != number:
# 	guess = check_for_challenged(guess)
# 	if guess < number:
# 		print "Hmm.. that seems a little too low to be the very best number."
# 	elif guess > number:
# 		print "Gee %r, the best number wouldn't be that high!" %name
# 	elif guess == number:
# 		print "Wowza, you know how to pick those numbers! Have you ever thought about a career in gambling?"
# 		break
# 	guess = raw_input("I bet you'll get the number this time: ").strip()
# 
# print "Now that you know that the best number is %d, it should be easy for you to win this game." %number
# print "You'll need to figure out the missing word."
# 
# missing = [
# ["feather", "boa", "constrictor", "A relative of this programming language", "It's a type of snake"], 
# ["cardboard", "box", "seats", "What IKEA furniture comes in", "Rhymes with fox"], 
# ["mating", "call", "waiting", "Something you do to a function", "What phones were intended to do, before data plans"],
# ["diving", "board", "of directors", "'Cranium' is this kind", "Rhymes with lord"],
# ["flip of a", "coin", "collector", "You probably have some in your pocket", "You use this for parking meters and laundry"],
# ["lend a helping", "hand", "sanitizer", "It contains your digits", "You have one at the end of each arm"],
# ["meteor", "shower", "curtain", "You may smell someone who needs this", "Rhymes with power"],
# ["pajama", "party", "pooper", "You've probably been to one of these events before", "It's a fiesta"],
# ["the time of my", "life", "insurance", "Along with liberty and the pursuit of happiness", "You're living it"]
# ]
# for s in range(3):
# 	x = random.randint(s*3,(s*3)+2)
# 	counter = 0
# 	print "Here's your clue:\n" + missing[x][0] + " " + "_" * len(missing[x][1]) + " " + missing[x][2]
# 	word = raw_input("Take a guess: ").strip().lower()
# 	while word != missing[x][1]:
# 		counter += 1
# 		if counter == 3:
# 			print "That's a hard one. Here's a hint -- " + missing[x][3]
# 		elif counter == 6:
# 			print "It's okay, everyone has different strengths. Here's your last hint -- " + missing[x][4]
# 		else:
# 			print "Hmm... that's an interesting idea..."
# 		word = raw_input("Take another guess: ")
# 	print "You ROCK, nobody gets that right! Congratulations."
# 
# print "You are a word ninja and will now be elevated to the next level. It's kind of blowing my mind."
# print "In this game, we'll test if you are quick enough, %s. You must get most answers right to move on." %(name)
# 
# mathcount = 0
# operators = {"+" : operator.add, "*" : operator.mul, "/" : operator.div, "-" : operator.sub}
# while mathcount < 5:
# 	print "Let's try a new round."
# 	raw_input("Press enter to begin! ")
# 	print "-----------------------------------"
# 	mathcount = 0
# 	for x in range(0,8):
# 		n = random.choice(operators.keys())
# 		num1, num2 = random.randint(1,20), random.randint(1,5)
# 		s = random.randint(2,10)
# 		prompt = "You have %d seconds. Solve: %d %s %d = " %(s, num1, n, num2)
# 		answer = raw_input_with_timeout(prompt, s)
#  		if not (answer):
#  			pass
# 		elif check_guess(answer) == True and int(answer) == int(operators[n](num1, num2)):
# 			print "On fire!"
# 			mathcount += 1
# 		else:
# 			print "Nope. :("
# print "You have proven yourself worthy."
print "Now your hard work has paid off and you will be rewarded."

# last round?
# how to celebrate winning? -- computer sings song?

