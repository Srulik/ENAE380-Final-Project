#Pasternak, Anthony and Smith, Michael
#ENAE380 Section 0203
#Final Project
#Professor Mumu Xu

from tkinter import *
import time
import os

#Global variable storing values for whether or not user answers questions correctly
qr = []

#Starting Values for score.
health = 100
time_spent = 0
morale = 50

#Class for User Interface for Short Answer Questions
class ShortAns(Frame):
    def __init__(self, que, ans, master=None): #Initialize class given Tk window, question, and answer
        #set question and answer to local variables
        self.question = que
        self.answer = ans
        
        Frame.__init__(self,master)
        self.pack() #Pack frame into window
        
        self.createWidgets() #Run function to create the widgets
        
    def createWidgets(self):
        #Create Label that asks the question and pack into window
        self.label = Label(self)
        self.label["text"] = self.question
        self.label.pack()

        #Create Answer Box to hold user input and pack into window
        self.ansbox = Entry(self)
        self.ansbox["width"] = len(self.answer[0])+10
        self.ansbox.pack()

        #Create Submit button, and call submit function when pressed; pack into window
        self.submit = Button(self,text="Submit",command = self.subans)
        self.submit.pack()

    def subans(self): #Submit function
        userans = self.ansbox.get() #get user input from answer box
        global qr #refer to list variable to store correct/incorrect

        if userans.lower() in self.answer: #check answer and store true/false value in list
            qr.append(True)
        elif userans.lower() == self.answer[0].lower():
            qr.append(True)
        else:
            qr.append(False)

        #Close window after user submits answer
        global w
        w.destroy()

#Class for User Interface for Multiple Choice Questions
class MultiChoice(Frame):
    def __init__(self, que, opt, ans, master=None): #Initialize class given Tk window, question, and answer
        #set question and answer to local variables
        self.question = que
        self.options = opt
        self.answer = ans
        self.buttSize = len(sorted(self.options, key = len)[-1])+10
        
        Frame.__init__(self,master)
        self.pack() #Pack frame into window
        
        self.createWidgets() #Run function to create the widgets
        
    def createWidgets(self):
        #Create Label that asks the question and pack into window
        self.label = Label(self)
        self.label["text"] = self.question
        self.label.pack()

        #Create Answer Buttons to hold user input and pack into window
        self.butt1 = Button(self)
        self.butt2 = Button(self)
        self.butt3 = Button(self)
        self.buttons = [self.butt1, self.butt2, self.butt3]

        counter = 0

        for x in self.buttons:
            x["text"] = self.options[counter]
            x["width"] = self.buttSize
            if counter+1 == self.answer:
                x["command"] = self.subans
            else:
                x["command"] = self.leave
            counter += 1
            x.pack()
            
    def subans(self): #Submit function
        global qr
        qr.append(True)
        
        global w
        w.destroy()

    def leave(self):
        global qr
        qr.append(False)
        
        global w
        w.destroy()

#Function for a dramatic scroll between blocks of text
def dramaticPause():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

#Clear Terminal Screen function compatible with all systems
    #By popcnt on Stack Overflow
    #https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



#Get User's Name for Result Document
name = ""

while name == "":
    name = input("Please Enter your Name: ")

cls()

#Intro
input("""
Welcome to C/Pasternak and C/Smith's interactive combat scenario!

You will be following the events that occur and answering Warrior Knowledge Questions in order to successfully
complete your mission on time and keep your team happy and healthy.

Press Enter to begin, and Good Luck!
""")

cls()

#Begin Story
print("You are a newly commissioned Second Lieutenant in charge of leading a \nsmall group consisting of two fireteams of 4 enlisted airmen each into enemy territory.")
dramaticPause()

print("You will be leading your group into the far east nation of Southern Milouperia, a country whose \nDemocratic government is being challenged by a group of Communist rebels who are backed by rival nation Raquru.")
dramaticPause()

print("In the midst of this proxy war your team must extract some vital information \nthat intel has revealed is being kept in a compound in the capital city of Ruwa.\n")
time.sleep(2.5)
input("Press Enter to Continue...")
cls()

print("""
Your Squadron consists of the following Airmen:

Fireteam Victor
Team Leader - Staff Sergeant Torres
Automatic Rifleman - Senior Airman Price
Grenadier - Senior Airman Green
Rifleman - Airman First Class Barnes

Fireteam Whiskey
Team Leader - Staff Sergeant Clark
Automatic Rifleman - Senior Airman King
Grenadier - Senior Airman Adams
Rifleman - Airman First Class Sullivan
""")
input("\nPress enter to Continue...")
cls()

print("""
Your performance will be analyzed using the following statistics:

Health - Keep your squadron safe and avoid casualties. You will start with 100 health.

Time - Making poor decisions will waste time, the quicker the mission is executed, the better. \nYou will start at 0 hours, a perfect score will result in the mission being accomplished in 7.5 hours

Morale - Keep your squadron’s spirits up. You will start with 50 morale and can go up or down from there.\nA perfect score will result in 110 morale.
""")
time.sleep(2.5)
input("Press Enter to Continue...")
cls()





#Question 1

#Creates Tkinter Window for Question class
w = Tk()
w.geometry("400x300")

#Sets question and correct answers
quest = "Due to the importance of this mission, you have received \nyour orders directly from the Air Force Chief of Staff himself. \n\nWho is the Air Force Chief of Staff?"
corrects = ["General Charles Q. Brown Jr.", "general charles q brown jr.", "general charles q brown","general charles q. brown", "general charles q brown jr", "general charles q. brown jr"]

#Creates instance of question class and waits for an answer
q1 = ShortAns(quest, corrects, master = w)
q1.mainloop()

#Different result display depending on whether question answered correctly or incorrectly
if qr[-1] == True:
    morale += 5
    print("Well done, your team morale has increased by 5 points.")
else:
    morale -= 5
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team morale has decreased by 5 points.")

#Displays current status of performance statistics    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()






#Question 2

w = Tk()
w.geometry("500x300")


quest = """Your group will be boarding an AC-130 at Joint Base Pearl Harbor-Hickam, Hawaii 
	before flying to Southern Milouperia. 

	What MAJCOM is located at this base?"""
options = ["Air Mobility Command", "Air Force Special Operations Command", "Pacific Air Forces"]
corrects = ["Pacific Air Forces"]

q2 = MultiChoice(quest, options, 3, master = w)
q2.mainloop()

if qr[-1] == True:
    morale += 5
    print("Well done, your team morale has increased by 5 points.")
else:
    morale -= 5
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team morale has decreased by 5 points.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 3

w = Tk()
w.geometry("500x300")


quest = """Before boarding the plane to fly to the warzone, you give a speech to your men 
where you remind them of the Air Force Core Values.

What are the Air Force Core Values?"""
options = ["Integrity, Service, Excellence", "Bravery, Obedience, Loyalty", "Trustworthiness, Teamwork, Flexibility"]
corrects = ["Integrity, Service, Excellence"]

q2 = MultiChoice(quest, options, 1, master = w)
q2.mainloop()

if qr[-1] == True:
    morale += 5
    time_spent += .25
    print("Well done, your team morale has increased by 5 points, and quarter of an hour has passed.")
else:
    morale -= 5
    time_spent += .5
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points, and a half hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()



#Question 4

w = Tk()
w.geometry("500x300")


quest = """Midway through the flight, somewhere over the pacific ocean, \nFireteam Whiskey is debating what the letter “H” \nis in the phonetic alphabet. SrA King says \nit’s “Hospital”. SrA Adams is sure it’s “Henry”. \nWhile A1C Sullivan thinks it’s “Hotel”.

Settle the debate and let them know \nwhich one is right."""
options = ["SrA King", "SrA Adams", "A1C Sullivan"]
corrects = ["A1C Sullivan"]

q4 = MultiChoice(quest, options, 3, master = w)
q4.mainloop()

if len(qr) != 4:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += .5
    print("Well done, your team morale has increased by 5 points, and half an hour has passed.")
else:
    morale -= 5
    time_spent += 1
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points, and an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 5

w = Tk()
w.geometry("500x300")


quest = """Half an hour before drop time, the AETC \nCommander calls to wish you good luck on \nyour mission.

What is the rank of the AETC Commander?"""
options = ["Brigadier General", "Major General", "Lieutenant General"]
corrects = ["Lieutenant General"]

q5 = MultiChoice(quest, options, 3, master = w)
q5.mainloop()

if len(qr) != 5:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    print("Well done, your team morale has increased by 5 points.")
else:
    morale -= 5
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 6

w = Tk()
w.geometry("400x300")

quest = "Your group is now 10 minutes out from parachuting \ninto an active combat zone. Recite the first \nstanza of the Airman’s Creed with your men to boost \nmorale before entering the warzone. (use all caps \nand correct punctuation)"
corrects = ["I AM AN AMERICAN AIRMAN. I AM A WARRIOR. I HAVE ANSWERED MY NATION’S CALL.", "I AM AN AMERICAN AIRMAN. I AM A WARRIOR. I HAVE ANSWERED MY NATIONS CALL."]

q6 = ShortAns(quest, corrects, master = w)
q6.mainloop()

if len(qr) != 6:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    print("Well done, your team morale has increased by 5 points.")
else:
    morale -= 5
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team morale has decreased by 5 points.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 7

w = Tk()
w.geometry("500x300")


quest = """You land half a mile from the target drop site \nunder the cover of darkness, you and your men \nmust travel quickly to the destination to \nbegin your mission.

At what position should you carry your rifles?"""
options = ["low ready", "high port", "low port"]
corrects = ["high port"]

q7 = MultiChoice(quest, options, 2, master = w)
q7.mainloop()

if len(qr) != 7:
    qr.append(False)

if qr[-1] == True:
    time_spent += .5
    print("Well done, your squadron travels quickly and half an hour has passed.")
else:
    time_spent += 1
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron travels slowly and an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 8

w = Tk()
w.geometry("500x300")


quest = """You must now cross a field covered in tall grass \nthat is overlooked by guard towers with rebel snipers who \nwill detect the slightest movement. You must decide how \nto cross the field.

How should you cross the field?"""
options = ["high crawl", "low crawl", "bounding movements"]
corrects = ["low crawl"]

q8 = MultiChoice(quest, options, 2, master = w)
q8.mainloop()

if len(qr) != 8:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, your squadron crosses the field in the most efficient manner and quarter of an hour has passed.")
else:
    time_spent += 1
    health -= 10
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron crosses the field ineffectively and is injured along the way, losing 10 health; an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 9

w = Tk()
w.geometry("500x300")


quest = """En route you encounter a narrow canyon \nonly wide enough for a few people to \nwalk side by side.

What squadron formation must you use \nto traverse the canyon?"""
options = ["squadron line", "squadron column", "squadron file"]
corrects = ["squadron file"]

q9 = MultiChoice(quest, options, 3, master = w)
q9.mainloop()

if len(qr) != 9:
    qr.append(False)

if qr[-1] == True:
    time_spent += .5
    print("Well done, your squadron traverses the canyon in the most timely manner and a quarter of an hour has passed.")
else:
    time_spent += 1
    health -= 10
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron takes a lot of time to traverse the canyon and is injured along the way, losing 10 health; an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 10

w = Tk()
w.geometry("400x300")

quest = "You arrive at the destination, an urban environment. \nRemind your squadron what the name of the technique \nused to secure building corners is called."
corrects = ["pieing the corner", "pieing a corner", "pieing the corner"]

q10 = ShortAns(quest, corrects, master = w)
q10.mainloop()

if len(qr) != 10:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, your team moves quickly; a quarter of an hour has passed.")
else:
    time_spent += .5
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team moves slowly; half an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 11

w = Tk()
w.geometry("500x300")


quest = """Your squadron is crossing an alleyway when SSgt Torres \ntrips which alerts nearby rebels. You start to take on heavy \nfire and SrA Green is shot in the leg.

What do you do?"""
options = ["return fire and take cover", "drop what you are doing and treat casualty", "drop your weapons and abort the mission"]
corrects = ["return fire and take cover"]

q11 = MultiChoice(quest, options, 1, master = w)
q11.mainloop()

if len(qr) != 11:
    qr.append(False)

if qr[-1] == True:
    time_spent += .5
    print("Well done, this is the correct action to take; half an hour has passed.")
else:
    time_spent += 1
    health -= 10
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron remains under fire and you lose 10 health, an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 12

w = Tk()
w.geometry("500x300")


quest = """You discover that SrA Green’s wound is capillary bleeding.

How do you treat this?"""
options = ["apply direct pressure and wrap in a bandage", "use a tourniquet", "amputate the limb"]
corrects = ["apply direct pressure and wrap in a bandage"]

q12 = MultiChoice(quest, options, 1, master = w)
q12.mainloop()

if len(qr) != 12:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, that is the correct care to implement; quarter of an hour has passed.")
else:
    time_spent += 0.5
    health -= 20
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nSrA Green's condition worsen's resulting in losing 20 health; half an hour has passed.")
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 13

w = Tk()
w.geometry("500x300")


quest = """You arrive at a building you must clear. \nYour fire team is lined up to the right of the \ndoor on the outside.

Where must the first member of the fireteam move to \nclear upon entering the room?"""
options = ["left of the door", "right of the door", "straight ahead"]
corrects = ["left of the door"]

q13 = MultiChoice(quest, options, 1, master = w)
q13.mainloop()

if len(qr) != 13:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, your squadron effectively clears the room and quarter of an hour has passed.")
else:
    time_spent += .5
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron takes longer than it should to clear the room; half an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 14

w = Tk()
w.geometry("500x300")


quest = """You encounter a staircase, you send Fireteam Whiskey downstairs to the basement \nwhile you lead Fireteam Victor upstairs. Upon getting up \nthe stairs you are immediately surrounded by \nenemy rebels, guns drawn.

Which article of the code of conduct \ndeals with surrendering?"""
options = ["2nd article", "3rd article", "4th article"]
corrects = ["2nd article"]

q14 = MultiChoice(quest, options, 1, master = w)
q14.mainloop()

if len(qr) != 14:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += .5
    print("Well done, your team morale has increased by 5 points, and half an hour has passed.")
else:
    morale -= 5
    time_spent += 1
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points, and an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 15

w = Tk()
w.geometry("600x400")

quest = "You are brought by your captors to a secured room.\n The 3rd article of the code of conduct deals \nwith being captured. Recite the 3rd article\n of the code of conduct. (use correct capitalization\n and punctuation)"
corrects = ["If I am captured, I will continue to resist by all means available. I will make every effort to escape and aid others to escape. I will accept neither parole nor special favors from the enemy."]

q15 = ShortAns(quest, corrects, master = w)
q15.mainloop()

if len(qr) != 15:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += .5
    print("Well done, your team morale has increased by 5 points; half an hour has passed.")
else:
    morale -= 5
    time_spent += 1
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team morale has decreased by 5 points; an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 16

w = Tk()
w.geometry("500x300")


quest = """Inside the enemy’s secured room you and Fireteam Victor \nbegin to be questioned by the rebels.

According to the 5th article of the code of conduct, \nwhat information are you required to give?"""
options = ["country and rank", " name, rank, service number, date of birth", "service number, orders, rank, names of everyone in your command"]
corrects = [" name, rank, service number, date of birth"]

q16 = MultiChoice(quest, options, 2, master = w)
q16.mainloop()

if len(qr) != 16:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += 1
    print("Well done, your team morale has increased by 5 points, and an hour has passed.")
else:
    morale -= 5
    time_spent += 2
    health -= 10
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points and the tortuting continues, you lose 10 health; 2 hours have passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 17

w = Tk()
w.geometry("500x300")


quest = """From the rebels who have captured you, \nyou learn that your cover had been blown which is why \nthey were prepared when you entered the top floor of the compound. \nYou realize that if you escape you must report this information \nto your commander at the Air Force Special Operations MAJCOM.

At which base is this located?"""
options = ["Wright-Patterson AFB, Ohio", "Robins AFB, Georgia", "Hurlburt Field, Florida"]
corrects = ["Hurlburt Field, Florida"]

q17 = MultiChoice(quest, options, 3, master = w)
q17.mainloop()

if len(qr) != 17:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += .5
    print("Well done, your team morale has increased by 5 points, and half an hour has passed.")
else:
    morale -= 5
    time_spent += 1
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points, and an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 18

w = Tk()
w.geometry("500x300")


quest = """Fireteam Whiskey, who you sent to clear the basement, \nbursts into the room and overwhelms your captors. \nYou secure the room and locate the targeted information \nin a nearby file cabinet. However while attempting to \nrescue you SSgt Clark has suffered a \nsucking chest wound.

What is the treatment for a sucking chest wound?"""
options = ["Have them bend over to reduce blood loss", "Cover the wound with an airtight bandage", "Leave him behind, sucking chest wounds are fatal"]
corrects = ["Cover the wound with an airtight bandage"]

q18 = MultiChoice(quest, options, 2, master = w)
q18.mainloop()

if len(qr) != 18:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, this is the correct care for a sucking chest wound; quarter of an hour has passed.")
else:
    time_spent += .5
    health -= 20
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nSSgt Clarks condition worsens and you lose 20 health; half an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 19

w = Tk()
w.geometry("500x300")


quest = """Despite your efforts to help SSgt Clark, \nhe is still unable to move on his own. \nYou have two men available to perform \ncasualty movement for SSgt Clark.

Which carry should you use?"""
options = ["one person drag", "fore and aft carry", "litter carry"]
corrects = ["fore and aft carry"]

q19 = MultiChoice(quest, options, 2, master = w)
q19.mainloop()

if len(qr) != 19:
    qr.append(False)

if qr[-1] == True:
    time_spent += .25
    print("Well done, you quickly transport SSgt Clark; quarter of an hour has passed.")
else:
    time_spent += .5
    health -= 10
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour squadron takes a long time to transport SSgt Clark and you lose 10 health; half an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()




#Question 20

w = Tk()
w.geometry("500x300")


quest = """As you carry SSgt Clark to the top of the compound which is \nthe extraction point you remind your squadron \nof this stanza of the Airman’s Creed: \n“I AM AN AMERICAN AIRMAN: \nWINGMAN, LEADER, WARRIOR. \nI WILL NEVER LEAVE AN AIRMAN BEHIND, \nI WILL NEVER FALTER, \nAND I WILL NOT FAIL.”

Which stanza of the Airman’s Creed is this?"""
options = ["2nd stanza", "3rd stanza", "4th stanza"]
corrects = ["4th stanza"]

q20 = MultiChoice(quest, options, 3, master = w)
q20.mainloop()

if len(qr) != 20:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += .25
    print("Well done, your team morale has increased by 5 points, and quarter of an hour has passed.")
else:
    morale -= 5
    time_spent += .5
    print("That is incorrect, the correct answer is " + corrects[0] + ". \nYour team morale has decreased by 5 points, and a half hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()


#Exposition between 20th and 21st question
success = False
if sum(qr) >= 15:
    success = True
    input("Your squadron is picked up by a group of Blackhawk helicopters from the extraction point \non the roof of the compound. SSgt Clark’s injuries are serious but you are told that he will live. \nYou have accomplished the mission and are flown back to be debriefed at Kadena Air Base, Japan. \nYou accomplished the mission despite the intel you received being compromised. Word of your outstanding leadership \nspreads and you are welcomed back to AFROTC Detachment 330 where you earned \nyour commission to talk at LLAB on a Thursday morning from 0600-0700. \n\nPress Enter to Continue.")
else:
    input("Your squadron is picked up by a group of Blackhawk helicopters from the extraction point \non the roof of the compound. SSgt Clark’s injuries are very serious and you are told that he will not survive. \n\nYou have failed your mission. You are flown back to be debriefed at Kadena Air Base, Japan. \n\nWord of your failure spreads and you are ordered to return to AFROTC Detachment 330 where you earned \nyour commission to speak at LLAB on a Thursday morning from 0600-0700. \n\nPress Enter to Continue.")

cls()

#Question 21

w = Tk()
w.geometry("500x300")

quest = "Who is the AFROTC Det. 330 Commander?"
corrects = ["Colonel Steven J. Jantz", "colonel steven j jantz", "Col Steven J. Jantz","col steven j jantz", "col steven j. jantz", "Col. Steven J. Jantz"]

q21 = ShortAns(quest, corrects, master = w)
q21.mainloop()

if len(qr) != 21:
    qr.append(False)

if qr[-1] == True:
    morale += 5
    time_spent += 1
    print("Well done, your team morale has increased by 5 points; an hour has passed.")
else:
    morale -= 5
    print("That is incorrect, the correct answer is " + corrects[0] + ". Your team morale has decreased by 5 points; an hour has passed.")
    
print("\nHealth: " + str(health) + "\nTime: "+ str(time_spent) + " hours\nMorale: "+ str(morale)+"\n")
input("Press Enter to Continue...")
cls()


#input(qr)



#qr = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

if success:
    mission = "Accomplished"
else:
    mission = "Failed"
results_text = "Your Results:\n\nMission "+mission+"\nHealth: "+str(health)+"/100\nTime: "+str(time_spent)+" hours.\nMorale: "+str(morale)+"/110\n"

total = sum(qr)
total_TCCC = sum([qr[10],qr[11],qr[17],qr[18]])
total_CoC = sum([qr[0],qr[4],qr[20]])
total_SUT = sum([qr[6],qr[7],qr[8],qr[9],qr[12]])
total_WK = total-(total_TCCC+total_CoC+total_SUT)

total_text = "You answered "+str(total)+"/21 questions correctly. This comes to "+ str(int(100*float(total)/21))+"%."
tccc_text = "You answered "+str(total_TCCC)+"/4 T-CCC questions correctly. This comes to "+ str(int(100*float(total_TCCC)/4))+"%."
coc_text = "You answered "+str(total_CoC)+"/3 Chain of Command questions correctly. This comes to "+ str(int(100*float(total_CoC)/3))+"%."
sut_text = "You answered "+str(total_SUT)+"/5 SUT/MOUT questions correctly. This comes to "+ str(int(100*float(total_SUT)/5))+"%."
wk_text = "You answered "+str(total_WK)+"/9 WK questions correctly. This comes to "+ str(int(100*float(total_WK)/9))+"%."

final_text = results_text+'\n\n'+total_text+'\n'+tccc_text+'\n'+coc_text+'\n'+sut_text+'\n'+wk_text

print(final_text)

name = name.replace(" ","_") + "_Warrior_Knowledge_GLP.txt"
result_file = open(name, 'w')
result_file.writelines(final_text)
result_file.close()
print
input("\nYour results have been stored in a file called "+name+". \nPress Enter to Finish.")
