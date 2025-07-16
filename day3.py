print(r'''
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::

''')
print("Welcome to The Castle.")
print("Your mission is to find the treasure.")
first = input("You're in front of two doors. Where do you want to go?(Left or Right)").upper()



if first == "LEFT":
    second = input(
        "There is a fire happening in front of you. Do you want to run through it or wait for it to set(Wait or Run.)").upper()
    if second == "WAIT":
        third = input('''You arrive at a ground unharmed. There is a big room with 3 doors.
        One red, one yellow and one blue. Which colour do you choose?''').upper()
        if third == "RED":
            print ("Game Over.You have been killed by the soldiers.")
        elif third == "YELLOW":
            print("You have found the treasure and won the game.")
            print ("Congrats")
        else :
            print ("Game Over.The Tigers got you.")
    else:
        print("Game Over.You have been burned to dust.")

else :
    print ("Game Over.You have fallen into a trap.")