goodchoices = ["Investigate the ominous door.", "walk through the doors", "Rest on the bench nearby.", "Resonate with the light of disco.", "Seek guidance from the adventurer's guild", "Set off immediately towards the temple", "Take the old wizard's advice", "Listen to the signs", "Follow the pathway to the familiar-looking temple."]
badchoices = ["Head straight towards the commotion.", "Open the cottage door", "Ignore the signs from the heavens.", "Break off a branch from the tree of life.", "Refuse help", "Steal the golden stone in the guild to get a wagon ride towards the forest.", "Brush off the old wizard's words.", "Ignore the omens.","Curse at the temple's deity."]
neutralchoices = ["Choose to continue investigating the dance floor.", "Return from whence you came", "Continue on.", "Leave the area you entered.", "Look out and reach to the sky.", "Ponder your situation and branch off", "Stare at him blankly", "Rest in the pond of life", "Kneel at the temple."]
goodevents = ["...", "The cottage remained silent, and the birds seemed to stop chirping. You decided to continue on. As you got closer to the town, wolves began to cry out in what seemed to be sadness and fury. ", "The starry sky covered you like a blanket that night. After waking up, you continue your journey and stumble into an area that contains a majestic tree. Fireflies gathered around the tree like faeries.", "You stood there in reverence, feeling the warmth from the tree wash over you. The fireflies began to glow harder. Some of the warmth felt like it was surrounding the very core of your being, and you felt invigorated and strong. You finished your journey to the town after your encounter with the tree.", "You were able to get directions to the temple in the holy forest and continued your journey on foot. Along the way, you saw a mysterious looking tower. In front of it stood a tall man with graying hair.", "You nod at the wizard's words. You are sure that you haven't made the best decisions before, but as long as you make up for it later on, you will likely be alright. As you continued on the path to the holy forest, the wind whispers to you: The end of your journey lies at the temple", "Eventually, you find yourself in front of the pond of life. There were lilies around the pond, symbolizing purity. Perhaps this is a sign to keep a clear conscience.", "You saw a sign on the road that said, 'Here lies the beaten path towards the end.' You follow the path with your eyes, with your vision resting on a glowing silver temple surrounded by forest.", " "]
badevents = ["As you fight your way through the crowd, you find that there is a dance battle going on. You watch and then decide to show off your groovy moves!", " The door creaks open, revealing an empty cottage. Something seems to rush out from it, but before you could look around, it was gone. You decide to continue on the path towards the nearby town.", "You journeyed through the dangerous night, evading monsters and dangerous animals that were in the way. You stumble into an area that contained a majestic tree. Fireflies gathered around the tree like faeries.", "Thunder rumbled ominously after the branch was obtained. You decide to ignore it and continue on.", "Along the way, you saw a mysterious looking tower. In front of it stood a tall man with graying hair. He turned to you, and spoke of his tale as one of the wizards from legend. He tells you to take care with your conscience, for it will be the key to the end of your journey.", "The wizard looked at you with disappointment. He seemed like he wanted to tell you something, but he refrained. You glanced back at him once you were already a while away. He was already gone.", "Eventually, you find yourself in front of the pond of life. There were lilies around the pond, symbolizing purity. Perhaps this is a sign to keep a clear conscience.", "You saw a sign on the road that said, 'Here lies the beaten path towards the end.' You follow the path with your eyes, with your vision resting on a glowing silver temple surrounded by forest.", " "]
neutralevents = ["You eventually reach a signpost that points towards the nearest town. A cottage on the side of the road attracts your gaze."," ", "n_event placeholder 3", "n_event placeholder 4", "Along the way, you saw a mysterious looking tower. In front of it stood a tall man with graying hair.", "n_event placeholder 6", "Eventually, you find yourself in front of the pond of life. There were lilies around the pond, symbolizing purity. Perhaps this is a sign to keep a clear conscience.", "You saw a sign on the road that said, 'Here lies the beaten path towards the end.' You follow the path with your eyes, with your vision resting on a glowing silver temple surrounded by forest.", " "]
#these are the events and choices that the player will encounter as they go through the game.

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
  print("\nThe fates whisper their will into your ear: " + var + "\n") 
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
  print("Everything around you begins to glow, and a warm breeze hits your face. You close your eyes, and a voice whispers to you: \n'You have broken the cycle. You are now free.'\nSuddenly, memories of the past cycles flood into your mind, with all the many choices you have made as your previous incarnations. Your soul cried out in joy, and you soared back to the stars, the place where your journey truly began. You no longer have to live the same cycle for eternity. The prize of freedom made you feel light, and you felt energy coursing throughout your entire being. \n'Welcome, child.'\nAn all too familiar voice behind you sounds throughout the gentle cosmos.\n'You are now one of us, in charge of the cyclical lives of humanity. You are free, but that freedom comes with responsibility. You may now guide others as I have done for you. \nAnd thus, you set off to guide a new soul. \n'Good luck, " + str(name) + ".'")
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
