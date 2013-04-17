"""Hello! Thank You for playing!
	
My name is Ben Bhamdeo and I am not a programmar. 
My background lies in the classics- Ancient Greek Civilization and Language. 
I also really like storytelling, films, literature and video games.
	
The following game has been made as a sort of 
review for myself as I learn python. Nevertheless, 
it is also meant to, hopefully, be as entertaining a 
game as possible. 

Given my background, I have chosen 
to focus on Story rather than on mechanics, and thus, this game
reads more like a short story than it does play like a game. 

The Plot has been Inspired by Bram Stokers,'Dracula'

Copyright 2013 Benjamin Bhamdeo

Please no stealing! Sharing is great, but please make sure to include a citation!

If you would like to reach me, you can email me at BenjaminBhamdeo@gmail.com

Cheers!"""


### Notes ###

"Preliminary Notes need to be updated as the game takes shape to maintain informality."
"Library/Bookcase/Book needs to be given Lore" 

### Notes ###


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m" ### contuine ### 
    OKGREEN = "\033[92m" #input###
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def opener():
	print "\n\n [TITLE]"
	print "A Simple Text Based Game"
	print "by Benjamn Bhamdeo\n\n"
	
	cont = raw_input(bcolors.OKBLUE + "Press Enter to Continue or cntrl - c to exit" + bcolors.ENDC)
	
	while cont != "":
		cont = raw_input( bcolors.OKBLUE + "Press Enter to Continue or cntrl - c to exit" + bcolors.ENDC)

def menu():
	print "\n||| Main Menu |||"
	print "\nTo Begin Playing, Enter 'play'"
	print "For More Information About This Script, Enter 'more'\n"
	
	counter = 0
	
	while counter != 1:	
	
		cont = raw_input(bcolors.OKGREEN + "Input >   " + bcolors.ENDC).lower()
	
		if cont == "play":
			counter += 1
		elif cont == "more":
			more_info()
			counter +=1
		else:
			print "\ninvalid input, please double check your response!\n"
		
def more_info():
	print "\n||| More Info |||\n"
	print """Hello! Thank You for playing!
	
My name is Ben Bhamdeo and I am not a programmer. 
My background lies in the classics- Ancient Greek Civilization and Language. 
I also really like storytelling, films, literature and video games.
	
The following game has been made as a sort of 
review for myself as I learn python. 

Given my background, then, I have chosen 
to focus on Story rather than on mechanics, and thus, this game
reads more like a short story than it does play like a game. 

Nevertheless, it is also meant to, hopefully, 
be as entertaining a game as possible. 

The Plot has been Inspired by and somewhat adapted 
from Bram Stoker's, 'Dracula'

Copyright 2013 Benjamin Bhamdeo

Please no stealing! Sharing is wonderful, but please make sure to include a citation!

If you would like to reach me, you can email me at BenjaminBhamdeo@gmail.com

Cheers!"""

	cont = raw_input(bcolors.OKBLUE + "Press Return to Play!" + bcolors.ENDC)
	
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Press Return to Play\n!" + bcolors.ENDC)
	
def prelim_notes():
	print "\n||| Premilinary Notes |||"
	print """
This game is very much text based. 
In other words, there are a lot of them (words, that is).
To assist in narrative pacing, during narrative sections
the Return Key shall be utilized as a 'continue' button. 

Every time the game's pacing is up to you, there should 
be an appropriately labeled prompt to let you know where you are.

Puzzles and riddles are solved via a looking for keywords in your answers.
These keywords should be important enough that your typing in a plethora
of responses should be considered acceptable so long as you hit one of 
those keywords. 

Press Return When You are Ready to Continue (and note the prompt for continue)"
"""
	cont = "placeholder"
	
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
	
def prologue():
	print "\n||| Prologue |||"
	print "\n\nJan. 27, 18--\n"
	print """ 
Heavy rain beats against the window as I write this entry, 
this entry that might be the last thing that will ever be heard of me 
forevermore. The thunder booms and roars and fiery bolts of lightning 
streak across the sky as swift and terrible as the hammer strikes the anvil...
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
I arrived at the town of Ortenburg, an old rustic town in, Bavaria, Germany, 
just last night and ever since have spent every waking hour preparing 
my soul to undertake the grim task that awaits me in this strange and 
foreign land.
"""
	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
		
	print """
For months, my home had been plagued by some malevolent spectre, 
an unseeable trepidation that cast a blanket of dread over myself and my 
friends and family. 

At first, the townsfolk and I thought nothing of the uncharacteristically
damp, gloomy weather, or of the aura of despair that seemed as if it were 
draining the very color form the world during what should have been a 
pleasant season.

We simply blamed mother nature for the weather and in turn, blamed the 
weather for our lowered spirits, continuing to live our lives as we only knew 
how.
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print "\nBut then people started dying...\n"

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
		
	print """
Those who died, all of them, died in the same mysterious fashion:  
with no warning, save a slight complaint of fatigue. Neither were 
they troubled by fever, nor could any physical marks be observed on 
their bodies. No expression of even a slight pain did they wear until
their demise.  

When death had crept over them and their lives wholly waned beyond
recall, an eerie observation could be made, undoubtedly a reaction to the
means by which they had been consumed.

When discovered, the victims all lay in their beds, their eyes wide open and
with their pupils fully dilated, seeming to state through the air towards a 
void where no spirit had e'er tread. They were ghotly pale, paler than even
the palest corpse. And most alarmingly, when one examined the bodies closer, 
he would find a small, pale blue make just near the heart.  
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
Nobody knew what these signs could possibly mean -- at least, 
nobody but Van Sloan. He was an odd sort of man, the 'crazy neighbor' 
type of man. From the moment that this shadow had settled upon the city, 
he could be heard whispering warnings...
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
'It's not natural, I tell ya. It's the work of some devilish thing. 
Something evil is afoot; something wicked... I'm sure of it'
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
Unfortunately for me, he was MY neighbor... and so when he was driven 
to pursue his theory at the behest of these killings, I was the first 
he rallied to his cause. 
"""
	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
	
	print """
Old man Van Sloan said that he had seen these signs before when 
he was a doctor in Germany, though that he hadn't seen or heard 
of this phenomenon in decades. 

I, myself being a Doctor, was curious as to what novel disease he 
could have been speaking of, an illness that I had never before 
encountered nor read about. 

I was surprised and appalled then, at his explanation of 
the true cause of this malady. 
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
'This illness is no earthly sickness. It is the result of a ghastly 
devouring,' he began. 

'Long ago, certain men and women had succeeded in creating feats of sorcery.
Some of these feats were used for the good of all. But those practitioners 
grew greedy and fearful and began to pervert these once noble means.'

'One particular form of magic, while granting longevity and near immortality 
came at an inhumane price. One must forfeit his or her soul and feed on
the life essence of others.'

'This wicked chill that has been hanging over our city, it is his way of 
feeding on our energy. As we wane, he is sustained. But he cannot thrive 
on this form of siphoning, alone. No, he must also feed wholly on individuals, 
slowing stealing their life so that he might continue his.'

'This is how they died... I am sure of it. Why he has come here, I do 
not know, but he must be repelled.'
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
I listened as he explained to me how as a medical student in Germany 
he had taken up residency in a town that had suffered from the same affliction, 
but that, alas, when he had finally learned the true cause of these 
deaths, it was too late: whatever dark artist had been consuming 
these people had vacated the city and ne'er returned.  

He told me how he hunted him and learned of his castle in the black forest, 
very near to where I write from now, but that upon seeking out the fiend so 
that he might put an end to him, that he could not summon the courage to go 
through with the journey through that frightening haunt. 

And thus, he fled to England, where he thought he might live out the rest 
of his days hiding from the shame he felt over not riding the world of this 
evil.

'But not any longer,' he concluded, rallying himself, 'for fate has given me 
a second chance, and I will answer its call valiantly!'
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
		
	print """
I hadn't heard from him for days after speaking to me, but then about a week 
later, the worst had happened. I received a call from him one night during
which he had informed me that after tracking the sorcerer to his local lair, 
he attempted to kill the fiend, but was unsuccessful in overwhelming him. 

While grappling with him, he felt a sharp incision near the base of his chest. 
At first, he thought he had been stabbed but upon the parasites' flight, he had 
noticed that it was not so, although he felt a pulsating pain, nonetheless. 

He had been marked with some sort of poison and was being consumed
from the inside out. 
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
		
	print """
Knowing that his time was short and his death was imminent, he then asked a favor 
of me that I regret having granted.

I have agreed to travel here in his place and put an end to this creature's 
monstrous wraithlike consumption. 
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
I have been reading the books that the Doctor has given me and my plan 
of attack is clear. 

I must enter his home and find my way to his bedroom while he slumbers. 
For, although possessing great powers, the sorcerer can only function 
under the shade of night time, as the sun provides him with unbearable pain, 
that, if bore for long enough, would end him.  

Once there, I must do what needs to be done for the sake of all mankind 
and to avenge my fallen countrymen. 

And thus as the sun now rises I make my leave so as to catch that 
monster of a man while he recuperates from his dark affairs...
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

def castle_entrance():

	print """\n|||  Castle Approach  |||

After an hour of walking uphill in the woods, 
following the map that the Doctor has left you, 
you have wandered upon a small opening, inside of 
which lies your destination.

The castle is rather tall, although not very wide, 
a lonely graphite pillar standing watch over the equally 
as dark trees of the bleak forest.

You walk towards the imposing front door and, surprisingly, 
it's open. It doesn't seem that the sorcerer ever expected company.
"""
	
	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """\n||| Entrance Hall ||| 

The entrance hall is dimly lit by a handful of torches. 
A chandelier hangs at the room's center, the wax candles 
all burnt down to the very bases of their wicks.  

Lining the walls are dusty suits of Armor and Trophy Cases 
displaying old swords and jewelry. An ancient Persian Rug lies 
on the stone floor, a burgundy accent against the grey stone. 

In another time, this might have been quite a warm and lavish room, 
but not any longer. 

In front of you is a grand staircase rises towards one relief 
before separating to the left and the right. 

There are doors on either end, a Right Door and  Left Door.
"""
	door = "unopened"
	key = 0 
	mace = 0 
	
	while door != "opened":	
		
		user = raw_input(bcolors.OKGREEN + "You are standing in the hall, what do you do?" + bcolors.ENDC)
		
		if "rug" in user.lower():
			print """
The Rug is elaborate and obviously very old,
but beyond that there is nothing interesting about it.
Best look around more. 
"""
		
		elif "stair" in user.lower() or "staircase" in user.lower():
			print "\nThere are two doors at the end of the staircase\n"
		
		elif "armor" in user.lower() or "suit" in user.lower():
			print "\nThe suit of armor is holding a large mace\n"
			
			response = raw_input(bcolors.OKGREEN + "What do you do with it?" +bcolors.ENDC)
			
			if "take" in response.lower() or "mace" in response.lower():
				print "\nYou have aquired a mace and returned to the room\n"
				mace = 1
			else:
				print "\nYou return to look around the room\n"
		
		elif "case" in user.lower() or "trophy" in user.lower() or "display" in user.lower():
			print "\nThis case has a regal looking sceptre in it\n"
			print "But you also seem to notice a golden Key alongside it.\n"
			
			response = raw_input(bcolors.OKGREEN + "What do you do with it?" +bcolors.ENDC)
			
			if "take" in response.lower() or "key" in response.lower():
				print "\nYou have aquired a Key and returned to the room\n"
				key = 1
			else:
				print "\nYou return to look around the room\n"
		
		elif "left door" in user.lower():
			print """
You open the door to find quite a large and elaborately decorated hearth.
The walls of the living room, upon which there are 2 large portraits, one of a man
and the other of a woman, are a dark mahogany color and the same
sort of lavish rug lies on the ground in this room. The room is dimly lit
and it is obvious that a fireplace had been burning not but a few hours ago

Having explored the room, however and finding nothing of interest, 
you return to the main hall.
"""

		elif "right door" in user.lower() and key == 1:
			print "\nThe Right Door is locked\n"
			print "However, you insert the key that you found and..."
			print "\n*CLACK* The door opens and you press on.\n"
			door = "opened"
		
		elif "right door" in user.lower() and mace == 1:
			print "\nThe Right Door is Locked\n"
			print "However, you bash the mace upon the lock."
			print "The old bolt breaks inside of the wooden slab."
			print "\nIt swings open and you press on\n"
			door = "opened"		
		
		elif "right door" in user.lower():
			print "\nThe Right Door is locked\n"
			print "You'll need to find a way to open it.\n"

def library():
	print """
There is a wide, long hallway on the other end of the door.
You walk into the corridor and get the strangest impression 
that it's actually making itself longer as you walk down it.
Nevertheless You reach the end of the dark causeway only to find 
quite the surprising sight.
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """ \n||| Library |||\n 
The next room is quite large, with dozens of Bookcases lining the walls.
All of them are filled with Dusty Tomes. At the end 
of the room, there is a handsome cheerywood Desk. Despite the fact
that the rest of the castle seems quite shrouded in darkness,
this one room features several open Curtains,
letting in the soft, warm morning sunlight -
It seems as if the sorcerer enjoyed reading by the moonlight.\n"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
	
	print """
Something can't be right though. 
It's a dead-end. 
"""	
	
	door = "unoppened" 
	curtains = "open"
	nightstand = "hidden"
	
	while door != "oppened":
		
		user = raw_input(bcolors.OKGREEN + "You are standing in the middle of the Library. What do you do?" + bcolors.ENDC)
		
		if "cherry" in user.lower() or "wood" in user.lower() or "desk" in user.lower():
			print """
You walk up the desk expecting to find something of use in it,
but strangely enough, not only is there nothing of worth, but the 
desk is entirely empty. 
""" 
				
		if "book" in user.lower() or "case" in user.lower():
			print """
The Bookcase looks ancient. Who knows how old it actually is.
Unlike the other bookcases, however, this particular bookcase seems to 
be devoid of cobwebs. It must be referenced frequently. While scanning
the titles you notice one of interest:

Most Dark Arts
"""
			response = raw_input(bcolors.OKGREEN + "Do you want to read it?" +bcolors.ENDC)
		
			if "yes" in response.lower() or "read" in response.lower():
				print "SOMETHING SPOOKY HERE"		
		
		if "dust" in user.lower() or "tome" in user.lower():
			print """
There are probably hundreds of books in this room.
You could go through all of them, but that doesn't 
seem like a wise use of your time at them moment. 	
"""		
		if "curtain" in user.lower() and curtains == "closed":
			print "\nyou've already closed the curtains\n"
		
		elif "curtain" in user.lower() and curtains == "open":
			print """
You examine the Curtains. 
They are quite lavish and heavy, but
you think you can manage to close them.
"""
			response = raw_input(bcolors.OKGREEN + "What do you want to do?" + bcolors.ENDC)
			
			if "close" in response.lower():
				print """
You close the Curtains on each of the windows. 
As the last bit of light leaves the room, you notice
a Erie green glow coming from the small nightstand at the 
center of the room.
"""				
				curtains = "closed"
				nightstand = "found"
		
		elif "nightstand" in user.lower() or "stand" in user.lower() or "night" in user.lower() and nightstand == "found":
			print"""
The green marks on the nightstand look strangely like 
fingerprints As you look closer you notice that they are 
concentrated around the knob of a drawer. 
"""			
			response = raw_input(bcolors.OKGREEN + "What do you want to do?" + bcolors.ENDC)
			
			if "open" in response.lower() or "pull" in response.lower() or "knob" in response.lower():
				print """
You pull the drawer out and hear a sliding noise coming
from the other side of the room. One of the bookcases has moved!
Behind it is a winding staircase descending into the bowels
of the castle. With a heavy heart, you press on... 
"""
				door = "oppened" 
		
		cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
					
def dungeon_entrance():
					
	print """ \n||| Dungeon Entrance |||
	
As you trundle down the winding stairs
you begin to notice more and more light 
as you reach the exit. But this is no
natural light
"""

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)

	print """
As you turn around the final corner in the 
spiral descent, you are greeted by an 
entirely black room shaped like a pentagon. 
Indeed, it looks as if the 
the dungeons have been made out of some sharp 
hellish obsidian.
"""			

	cont = "placeholder"
	while cont != "":
		cont = raw_input(bcolors.OKBLUE + "Continue..." + bcolors.ENDC)
		
	print"""
In the center of the ceiling, a jet black chandelier hangs,
its candles emanating dancing, bright green flames. 

There is a metal gate at the opposite end of the room, sealed shut.
Beyond it, you can see another passageway. 
In the corner closest to you, an iron maiden stands, completely shut. 
There are tables lined up against the walls with all sorts
of brutal instruments on them.
"""

	door = "closed"
	lever = "unfound" 
	maiden = "closed"
	coprse = "" 
	axe = ""
	arm = ""
	
	while door != "open":
		
		user = raw_input(bcolors.OKGREEN + "What do you want to do in the room?" + bcolors.ENDC).lower()
		
		if "table" in user:
			print """
You approach one of the tables. There are an 
assortment of weapons on it.			
"""
			response = raw_input(bcolors.OKGREEN + "What do you want to do with them?" + bcolors.ENDC).lower()
			
			if "take" in response:
				print """
You pick up an axe the table. Maybe it'll come in handy.
"""
				axe = "had"
		
		elif "iron" in user or "maiden" in user:
			print """
You approach the Iron maiden. There is a lock on the front of it.
"""
			response = raw_input(bcolors.OKGREEN + "What do you want to do with the device?" + bcolors.ENDC).lower()	
			
			if "open" in response or "unlock" in response:
				print """
You open the door and to your disgust a corpse tumbles out 
onto you, which you let fall to the floor.
"""
				corpse = "floor"
 		
		elif "corpse" in user or "floor" in user and corpse == "floor":
 			print """
You examine the half decayed body laying on the floor
 """
 			response = raw_input(bcolors.OKGREEN + "What do you want to do with it?" + bcolors.ENDC).lower()
 				
 			if "take" in response: 
 				print """
You flinch as you do it, but you twist the right arm 
and it snaps right off.				
"""
				arm = "had"
							
		elif user == "gate" and lever == "unfound":
			print """
You approach the iron gate. There's no way in hell you're
going to be able to lift it without finding a way to release the lock.
But in the corner of your eye you can see a level on the other end. 
You stick your arm through the grate but can't reach.
You'll need to find a way to get to it
""" 
			lever = "found"
		
		elif lever == "found" and user == "gate":
			print """
You stand before the gate. The lever is still out of your reach.			
"""
			response = raw_input(bcolors.OKGREEN + "What do you want to do with the gate?" + bcolors.ENDC).lower()
			
			if "arm" in response and arm == "had":
				print """
You stretch out the stiff arm and are just able to get its hand 
to slip around the lever. Pulling it backward releases the locking 
mechanism and the gate races upwards.
"""
				door = "open"
				
			elif "axe" in response and axe == "had":
				print """
You try and strike the gate the axe but it just ricochets off.
You're going to need to find another way to get through.
"""


### Order of Game###	


opener()
menu()
prelim_notes()
prologue()
castle_entrance()
library()
dungeon_entrance()