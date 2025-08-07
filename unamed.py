print("Gastillo opens his eyes — all 16 of them.")
print("He hears the fans in his head whirring as the implanted Spyder_Eys calibrate.")
print("The motion is nearly sickening, but he gets used to it.")

print("\nLooking around, he realizes he's been in cryostasis for about ten years.")
print("On the left side of the chamber, he sees a sticky note that reads: 'Open your codex.'")

print("\nHe checks his shirt pockets, then pants, and finally finds the codex in his boots.")
print("A message appears on the screen:")

print('''\n"Hey man, it's been a long slumber. You'll warm up eventually.
You were sent here by the big man up top to take over this Vastella ship.
You might’ve sustained some memory loss, but that’s okay.
This codex should catch you up to speed. Or don’t — it doesn’t really matter."''')

print('''\n "CODEX:"
The Kaizoku:

Ships: The ships that you will be using are the Blugills and Mantisellas. Better learn how to fly fast

Mantisellas: They look like flattened out hummingbirds. Primarily used by Sabrinen as suicide bombers or defenders. Also used going fast across planets or to different planets. But you aren't no mechanic don't go tinkering with this one.

Blugills: The best ship, fast, reliable and customizable. Always take one of these. It's also extremely simple to use.

Smugglers you'll likely come across:

Buq'ah:
Huge, fleeting ships are why they got their name. Primarily an offworld smuggling operation, they use Vastellas for everything. Our main and primary threat. It's kill on sight for these guys. They'll rep it in your face like nothing.

Lasiks: Get your hands on one of these puppies. They're valuable, trustworthy and very beautiful. Just be careful with your hands they'll burn.
''')

print('\n“Shit…” Gastillo mutters, his voice crackling with static.')
print("Confused, he touches his throat and feels wires and metal. Panicked, he breathes deeply, regaining some memory of his implants.")

print('\nA woman appears, peeking into the cryopod.')
print('"Hey dude, you can come out now. Do you need help?"')

# First choice
while True:
    answer = input("\nYes or No? ").lower()
    if answer == "yes":
        print("You step out with her, your hand around her shoulder, steadying yourself.")
        break
    elif answer == "no":
        print('''She pulls you out anyway, seeing your disheveled state.
You step out with her reluctantly, your hand around her shoulder, steadying yourself.
"Yeah man, I'm helping whether or not you want it. My name is Joseph. Odd name for a woman, so people just call me Jo."''')
        break
    else:
        print("Invalid answer. Try again.")

# Conversation continues
print('\nJo looks at you, semi-interested.')
print('"So, what’s your name?" she asks.')

print('"My name? It’s Gastillo," you respond.')

print('''\nShe looks at you in awe.
"Wow… I had no idea you were into cybernetics. You have Spyder_Eys and a VTB! So cool..."''')

print('\nGastillo chuckles. "Yeah, it’s... useful. But a pain in the ass."')

print('''\nYou both begin walking down a flight of stairs. 
The ship is massive — cryopods stacked to the ceiling, wide halls like a hotel.
You zoom in with your Spyder_Eys, estimating the ship holds hundreds of thousands, maybe millions.''')

print('\nJo notices you spacing out. "Hey dude, are you okay?"')

print('"Oh yeah..." you say.')

# Second choice
while True:
    answer = input("\nTell the truth? Yes or No? ").lower()
    if answer == "yes":
        print('''"I'm just looking for friends," you admit.''')
        break
    elif answer == "no":
        print('"Oh, just looking around," you say, deflecting.')
        break
    else:
        print('''She looks at you, confused.
"Jeez man, are you sure your brain didn't freeze?"
Invalid answer. Please try again.''')
