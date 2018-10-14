import random
import operator
import statistics
import math

# Setting up the parameters that women judge men on
maleheight = [178]
maleincome = [30000]
maleface = [5]
personality = ["Shy", "Nerdy", "Emotional", "Artistic", "Athletic", "Idealist", "Extroverted"]
race = ["White", "Black", "Indian", "Asian", "Latino"]

count = 0
while i < 250:
    maleheight.append(random.randint(160, 195))
    maleincome.append(random.randint(15000, 120000))
    maleface.append(random.randint(2, 10))
    count += 1

# Sample of males in the surrounding area.
print(maleheight)
print(maleincome)
print(maleface)

# Finding the averages
avgheight = sum(maleheight) / count 
avgincome = sum(maleincome) / count 
avgface = sum(maleface) / count 


# Finding the Standard Deviations
sdheight = statistics.stdev(maleheight, avgheight)
sdincome = statistics.stdev(maleincome, avgincome)
sdface = statistics.stdev(maleface, avgface)

# Interacting with the Femoids Hivemind interface
uname = input("Hi, I'm the Femoid Hivemind. What is your name?")

print("So " + uname + ", you want to know where you stand in the pecking order, do you?")
print("No problem. Just answer some of these questions and I'll tell you what the Femoid Hivemind thinks of     you.")
uheight = int(input("First off, how tall are you? [Enter height in centimeters, don't put units]"))
if uheight < (avgheight - (3 * sdheight)):
    print("Sorry, you are way too short cupcakes, but I know lots of girls that date short guys.")
else:
    print("Okay.")
uincome = int(input("How much money do you make? [Enter annual income, no commas or symbols]"))
if uincome < avgincome - ((3 * sdincome)):
    print("You make so little money? How can you handle a woman if you can't take care of yourself sweaty?")
else:
    print("Okay.")
uface = int(input("On a scale of 1 to 10, how attractive is your face?"))
if uface < 4:
    print("Sorry hun, maybe get a better personality?")
else:
    print("Thank-you.")
urace = input("What race are you? [Choose between White, Black, Indian, Asian or Latino]")
upersonality = input("And finally, what's your personality? [Choose between Shy, Nerdy, Emotional, Artistic,     Athletic,"
                     "Idealist or Introverted]")
print("Okay, all done. Let us process your information.")

# Tallying the scores
# Personality and race
PrefPersonality = random.choice(personality)
PrefRace = random.choice(race)
print("I like " + PrefPersonality + " guys.")
print("I like " + PrefRace + " guys.")

def compareaverage(average, personal, stddev):
    return round((average - personal) / stddev)

score = 5
# Height Tally
score += compareaverage(avgheight, uheight, sdheight)

# Income Tally
score += compareaverage(avgincome, uincome, sdincome)

# Face Tally
score += compareaverage(avgface, uface, sdface)
if upersonality == PrefPersonality:
    score += 1
if urace == PrefRace:
    score += 1

print(score)

# Final Determination
if score < 4:
    print("Sorry " + uname + ", you are subhuman.")
if score >= 4 and score <7:
    print(uname + ", you can be a betabux.")
if score >=7 and score <9:
    print(uname + ", you're the fuccboi I want to fuck on the downlow, but you're not really what I want.")
if score >=9:
    print(uname + ", you're the one I want forever")