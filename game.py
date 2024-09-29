goodchoices = ["Investigate the ominous looking door.", "Walk through the ominous looking door", "Talk to them.", "Continue on", "Follow the trail of tinsels.", 
"Decide to believe in their words", "Find the source of the usual light", "Investigate", "Follow the music into an unknown building."]

badchoices = ["Head straight towards the commotion.", "Break free from the dance floor and rush to the commotion.", "Head back to the dance floor and reinvestigate.", 
"You realize so much time has passed and feeling a sense of rush, you start running through the crowd.", "Decide not to follow the tinsels and talk to the security guards",  "Ignore their words as they seem too unreliable.", "Walk past the unusual light", "Ignore your discovery and turn back.","Walk back into the club."]

neutralchoices = ["Choose to continue investigate the dance floor.", "Look for clues nearby", "Continue on walking.", "You decide to take a break and step outside.", 
"Make a mental note of the trail, and decide to revisit later.", "You decide to keep their words at the back of your head", "Stare into the bright light", "Start slowly walking", "Ponder and rethink about the clues you have found."]

goodevents = ["You walk towards the door that caught your attention, when someone bumps into you and forces you to dance to a tune before moving on.", "As you walk through the ominous-looking door, you find that there is even fewer people here in this smaller room. However, someone is dancing alone in the middle of the room", "As you talk to them, they mention that they saw someone sneaking into the bathroom.", "You eventually reach the bathroom and there you find a trail of tinsels leading towards someplace.", "As you follow the trail, you end up in the a hidden alleyway in the back of the club. There you meet a random man yelling, \”oh the light, the light\”", "Believing their words, you look for something that fits the description and you see an unusual light gleaming in the distance", "After taking a closer look, you find a random car in the parking lot of the club.", "After further investigation, you find that someone had simply left their car lights on, but then you hear some music in the distance…,"," "]

badevents = ["As you fight your way through the crowd, you find that there is a dance battle going on. Before investigating further, you decide to show off your groovy moves!", "As you investigate, you find that there is a disco prodigy at the center of the commotion", 
"You find nothing new and decide to walk around the perimeter.",
 "As you are rushing, you stumble and fall to the ground and notice a trail of tinsels",
"The security guards had too much to drink and were of no help; however, one of the guards mentioned something about a pregnant looking man...", "Ignoring their words, you decide to head towards the parking lot where you see an unusual light", "Since you walked past the light, you could not discover any new clues and instead hear sirens in the distance.",
 "You follow the sirens and find that the police have discovered the disco ball in front of the club, but the person who had committed this crime was nowhere to be seen.", " "]

neutralevents = ["As you stay on the dance floor, the music gets the best of you and you start dancing along."," ", "n_event placeholder 3", "n_event placeholder 4", 
"As you step outside, you notice a trail of tinsels that appear to lead somewhere.", "n_event placeholder 6", "You continue walking, thinking about the clues you’ve found so far and you remember that you noticed an unusual light in the parking lot of the club", 
"You realize that the ball was hidden in the car with the bright light in the parking lot.", " "]

anschoice= 0
selects = []
tally= 0 
#These are the global variables used in later functions

def choicepopendtally(i):
  global tally
  global anschoice
  global pointtally
  if anschoice == 1:
    selects.append(goodchoices[i])
    pointtally= -3
    var=goodchoices[i]
  elif anschoice == 2:
    selects.append(neutralchoices[i])
    pointtally= 0
    var=neutralchoices[i]
  elif anschoice == 3:
    selects.append(badchoices[i])
    pointtally= 3
    var=badchoices[i]
  goodchoices.pop(0)
  neutralchoices.pop(0)
  badchoices.pop(0)
  tally= tally + pointtally
  print("\nThe disco gods whisper their will into your ear: " + var + "\n") 
  return tally
#This function takes the player's choice and appends it to the selects list. It also pops the used choices from the choices list so that there is conformity with what is displayed to the player.

def event_trigger(a, number):
  if a == 1:
    print(goodevents[number] + "\n")
  if a == 2:
    print(neutralevents[number] + "\n")
  if a == 3:
    print(badevents[number] + "\n")
#This function is called when an event needs to be triggered. It takes the number of the event's index in the list and prints the event.

def choices(choice1, choice2, choice3, num, number):
  global tally
  global anschoice
  print("You will... \n")
  print("1. " + choice1 + "\n")
  print("2. " + choice2 + "\n")
  print("3. " + choice3 + "\n")
  anschoice = int(input("Please select the number of your choice. Keep in mind that it must be between 1-3. \n\n"))
  while anschoice>3 or anschoice<1:
    print("Invalid selection. Please make another choice.")
    anschoice = int(input("Please select the number of your choice. Remember that it must be between 1-3. \n\n"))
  choicepopendtally(0)
  if num <len(goodevents):
    event_trigger(anschoice, number)
#This function allows the player to choose between the given choices. It saves that choice as anschoice and uses it to add to the tally variable in choicepopendtally()

print("Welcome to the Case of the Lost Disco Ball!")
name = input("What is your name? \n")
print("\nHello, " + name + "! In this world, you will be the detective faced with many choices to find the missing disco ball!")
print("Please choose wisely, as what you choose will determine the fate of the disco ball!")
print("However, don't forget to enjoy the music, as it won't last forever ;) \n")
print("--------------------------------\nGAME START\n--------------------------------")
print("\"Detective " + name + ", thanks for coming. As you can see, there's been a case here and we need your help.\" \nYou look around the surroundings and see that the dance floor is scarce and the usual disco ball is missing from its place. Suddenly, there is a loud commotion in the distance. \nYou look around and see another crowd on the other side of the room. But then, something catches your eye. You see a door that is slightly ajar, with rays of purple light shining through.")
#This is the context of the game

for i in range(9):
  choices(goodchoices[0], neutralchoices[0], badchoices[0],  0, i)




#Different endings are reached based on the value of the tally variable after the game ends.
if tally <= 5:
  print("After following the music into the random building, you find the disco ball in the center of the campus ballroom! It turns out that there was a hackathon going on, where the theme was Disco and they needed a disco ball so they had borrowed it from the club, but the club forgot. It was a huge misunderstanding, but thanks to you, the case was solved!")
#This is the good ending

if tally > 0 and tally < 12:
  print("Your vision goes dark. You wake up in a familiar floor of the ballroom, with a familiar voice whispering in your ears. You look around in confusion and tread to the doors that were opened in front of you.")
#This is the neutral ending

if tally >= 12:
  print("Suddenly, thunder strikes your body and you felt light. Somehow, you went airborne. You eventually come crashing down, meeting your demise at the edge of the dance floor, abandoned to the corner. You wonder, is this the end? Suddenly, a voice whispers to you. \n\n'This is only the beginning. Sleep my child, for your journey has not yet concluded.'\n\nQuietly, you felt yourself falling, falling into a crushing void. Your eyes open, exposing to your pupils a flash of colorful lights and you realize, this is where the lost, departed souls go before they are reborn after a failed journey, as well as the birthplace of such souls. You accept your fate and your mind goes blank, and you wake up in the middle of the dance floor. You remember nothing.")
#This is the bad ending

print("\n\n\n--------\nGAME END\n--------\n")
print("The soul of the disco remembers your decisions. Would you like to remember what you did on your journey?")
decision = int(input("1. Yes\n2. No.\n"))
if decision == 1:
  for i in range (len(selects)):
    print(f"{i+1}. {selects[i]}\n")
else:
  print(f"You decide not to look back and continue forward before the next part of the cycle begins.")

#Write code for trivia and also one you choose 3 bad choices, you have to quit game or restart

#This is the end screen of the game. The player can select whether or not they want to see the decisions they have made while playing. If they say yes, it will iterate through the selects list and print out each choice that was made.  
