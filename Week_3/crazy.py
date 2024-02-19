
yes_no = ["yes","no"]
direction = ["right","left","forwards","backwards"]
direction2 = ["right","left","forwards","backwards"]
directionmud = ["right","left","forwards","backwards"]
directionriver = ["right","left","forwards","backwards"]
direction3 = ["right","left","forwards","backwards"]

print("\nGreetings traveler!")
name = input ("What is your name?\n\n")

print("\nWhy hello there " +name+ ". It's a pleasure to meet you!")
print("\nNow now we don't have much time, let's begin.")

response = ""
while response in "":
    response = input ("Are you ready to go on this adventure? \nyes/no\n\n")
    if response == "yes":
        print("\nGreat! Lets begin!")
    elif response == "no":
        print("\nYou are not ready.")
        quit()
    else:
        print("\nI did not understand that.\n\n")
        response = ""

response = ""
while response not in direction: # ############# BEGINNING ############ #
    print("\n\nYou wake up in a forest.\nTo your right is a bear.\nTo your left is more forest.\nTo your front is a wall.\nTo your back is the exit.")
    response = input("\n(right,left,forwards,backwards)\n\n")
    if response == "right":
        print("\nThe bear ate you. You died.")
        quit()
    elif response == "left":
        print("\nYou walk deeper into the forest.")
    elif response == "forwards":
        print("\nYou can't climb the wall.")
        response = ""
    elif response =="backwards":
        print("\nYou run out of the forest. Coward.")
        quit()
    else:
        print("\nI did not understand that.\n")
        response = ""

dc1 = ""
while dc1 not in yes_no:
    dc1 = input("\n\nAs you walk deeper and deeper, you find yourself near a pond. Would you like to drink from it? \n(yes/no)\n\n")
    if dc1 == "yes":
        print("\nYou bend over to drink and accidently fall into the pond. You're now covered in mud and water.")
    elif dc1 == "no":
        print("\nYou walk away.")
    else:
        print("\nI did not understand that.\n")
        dc1 = ""

print("\n\nYou find yourself in a new part of the forest.\n")

dc2 = ""
while dc2 not in direction2:
    dc2 = input("\nTo your right is the village.\nTo your left is more forest. \nTo your front is a river. \nTo your back is the exit. \n(right,left,forwards,backwards)\n\n")
    if dc2 == "right" and dc1 == "yes":
        print("\nYou walk towards the village, but as you are covered in mud, the guard thinks you're a bear and shoots you down. You died.")
        quit ()
    elif dc2 == "right" and dc1 == "no":
        print("\nYou walk towards the village.")      ####Into village without being shot(Done)####
    elif dc2 == "left":
        print("\nYou walk deeper into the forest.")   #### Walking deeper into forest ####
    elif dc2 == "forwards" and dc1 == "yes":        ### Into the river with mud (Done)###
        print("\nYou walk towards the river and notice a bear there. The bear comes to attack but notices that you smell horrible because of the mud, and leave you be.")
        print("\nYou are now ")
    elif dc2 == "forwards" and dc1 == "no":
        print("\nYou walk towards the river and notice a bear there. It attacks you and eats you. You died.")
        quit()
    elif dc2 == "backwards":
        print("\nYou leave the forest. Coward.")
        quit()
    else:
        print("\nI did not understand that.\n\n")
        dc2 = ""

inmud = ""
while inmud not in directionmud:
    if dc2 == "right" and dc1 == "no":
        print("\n\nAs you walk into the village you notice the people look awfully more strange than normal. \nWhy are people dressed in halloween costumes, even though it's not halloween?\n\n")
        inmud = input("You look around and notice: \nTo your right is the barber shop with blood on the window pannels.\nTo your left is the grocery store with a clear view of a body on the floor.\nTo your front is deeper into the village. \nTo your back is the exit of the village. \n(right,left,forwards,backwards)\n\n")
        if inmud == "right":
            print("\nYou walk into the barber shop. The barber storms towards you and stabs the scissors in your neck. You bleed out and die.")
            quit()
        elif inmud == "left":
            print("\nYou enter the grocery store as you get shot by the cashier. You died.")
            quit()
        elif inmud == "forwards":
            print("\nAs you keep walking, you notice a figure appear behind you. He bites your neck and you slowly feel your soul leave your body. You died.")
            quit()
        elif inmud == "backwards":
            print("\nAs you try to leave the village, you notice a sign that you didn't see before reading 'No One Leaves Alive'. You sigh as you hear the guard cocks his gun. You died.")
            quit()
        else:
            print("\nI did not understand that.\n\n")
            inmud = ""

river = ""
while river not in directionriver:
    if dc2 == "fowards" and dc1 == "yes":
        print("\n\nYou continue walking along the river.")
        river = input("\n\nYou look around: \nTo your right is a couple of logs on the floor.\nTo your left is the bear.\nTo your front is more river.\nTo your back is back into the forest. \n(right,left,forwards,backwards)\n\n")
        if river == "right":
            print("\nYou walk up to the logs and pick them up. Only to find killer ants walking onto your arms. You died.")
            quit()
        elif river == "left":
            print("\nYou walk up to the bear again. The bear is now annoyed and decides to kill you either way. You died.")
            quit()
        elif river == "forwards":
            print("\nYou walk into the river only to get pulled by it. While along the current, your head hits a rock. You bleed out and die.")
            quit()
        elif river == "backwards":
            print("\nYou try to walk back into the forest only to get attacked by a snake. You died.")
            quit()
        else:
            print("\nI did not understand that.\n\n")
            river = ""

fr3 = ""
while fr3 not in direction3:
    if dc2 == "left":
        print("\n\nYou walk deeper into the forest.")
        fr3 = input("\n\nTo your right is a hut.\nTo your left is the beach (somehow).\nTo your front is more forest.\nTo your back is the exit of the forest. \n(right,left,forwards,backwards)\n\n")
        if fr3 == "right":
            print("\nYou walk towards the hut.")
            print("\nTo be continued...") ########################################
            quit()
        elif fr3 == "left":
            print("\nYou walk towards the beach.")
            print("\nTo be continued...") ########################################
            quit()
        elif fr3 == "forwards":
            print("\nYou walk deeper into the forest, only to be lost in it forever.")
            quit()
        elif fr3 == "backwards":
            print("\nYou leave the forest. Coward.")
            quit()
        else:
            print("\nI did not understand that.\n\n")
            fr3 = ""
