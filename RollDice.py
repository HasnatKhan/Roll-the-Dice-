import random

print("What do you want to bet on: ");
print("L less than 7");
print("E equal to 7");
print("G greater than 7");
choic = input("Enter choice (L, E, or G) : ");
print("Throwing dice...");
n1 = random.randint(1,6);
n2 = random.randint(1,6)
su = n1+ n2;
print(str(n1)+" and " + str(n2));
if (choic == "L"):
    if (su < 7 ):
        print("The total is "+str(su)+". You win");
    else:
        print("The total is "+str(su)+". You lose");
elif (choic == "E"):
    if (su == 7 ):
        print("The total is "+str(su)+". You win");
    else:
        print("The total is "+str(su)+". You lose");
elif (choic == "G"):
    if (su > 7 ):
        print("The total is "+str(su)+". You win");
    else:
        print("The total is "+str(su)+". You lose");
else:
    print("Invalid Input  ");
