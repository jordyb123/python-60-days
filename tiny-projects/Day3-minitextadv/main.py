#Mini Text Adventure Game
#Takes place in an abandoned lab
#It contains rooms, choices, consequences and endings

#Room 1: Entrance Hall
#Room 2: Research Wing
#Room 3: Security Office

#Endings: Good - You find the exit and escape before you get caught. Bad - Your spine gets ripped out of your mangled tortured body

#Flow: Entrance Hall -> Research Wing -> Security Office -> Ending



def main():
    start_game()

def start_game():
    print("Welcome to the Abandoned Lab!")
    print("After being lost in the snowy reaches of antartica for hours slowly freezing alive you stumble upon" 
    " an abandoned lab. The door creaks as you push it open, revealing a dimly lit entrance hall.")
    entrance_hall()

def entrance_hall():
    print("As you step inside the stench of sulfur and copper fills your nostrils and a sense of dread washes over you "
          ", the ground is covered in broken glass, discard lab equipment and the lights flicker ominously making it hard to see. "
          "You see two doors ahead of you. One leads to the Research Wing, and the other" 
          " to the Security Office. You also can't shake the feeling that you are being watched.")
    choice = input("Do you head to the Research Wing (1) or to the Security Office (2)? ")
    if choice == "1":
        research_wing()
    elif choice == "2":
        bad_ending()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        entrance_hall()

def research_wing():
    print("You cautiously enter the Research Wing, the air thickens with the smell of burnt flesh, chemicals and decay. The walls are painted red with "
          " what looks like blood, there are two decayed bodies slumped against the wall, the body of a long dead scientist in a chair broken test chambers"
          " and more blood on the floor. You see a containment chamber ahead of you that looks to be worth investigating, but you also notice a door "
          "marked above 'Secuirty Office' that you could also head towards.")
    
    choice = input("Do you investigate the containment chamber (1) or head to the Security Office (2)? ")
    if choice == "1":
        bad_ending()
    elif choice == "2":
        security_office()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        research_wing()


def security_office():
    print("You enter the Security Office, much like the other rooms you've been thus far it is dimbly lit and bloody. The only light is coming from "
          "a flashing computer screen, you also see a secuirty guard slumped over his desk, still gripping his shotgun but at the same time his back is completely"
          "torn open and his spine removed barbarically from ravaged body. You see another computer terminal still in operation that looks to have security footage."
          "Additionally you see a control panel with a big red button next to an emergency exit door.")
    
    choice = input("Do you check the security footage (1) or press the big red button and use the emergency exit (2)?")
    if choice == "1":
        bad_ending()
    elif choice == "2":
        good_ending()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        security_office()

def bad_ending():
    print("You suddenly feel a sharp pain from behind. You hear the ripping of your flesh and the cracking of your bones as you are thrown to the ground."
          "Then you feel your spine being ripped out as all feeling leaves your mangled body. You are now just a husk, food and sustinance for the creatures "
          "of the Abandoned Lab.")
    
def good_ending():
    print("You press the button and the emergency exit door slides open with a loud hiss. You step through into a long corridor, you can see the light "
          " coming from outside. You sprint towards the light and burst through to the outside world, you made it out for now...")


main()

