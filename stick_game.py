def stick_games():
    print("Welcome to the sticks Game!")
    print("Rules: You can pick 1,2,, or 3 sticks in one turn")
    print("The player who picks the last stick loses.")
    no_of_sticks=16
    player1= input("Enter name")
    player2=input("enter name")
    print("Games started!")
    remaining_sticks=no_of_sticks
    while remaining_sticks>0:
        print(f"sticks remaining:{no_of_sticks}")
        A= int(input(f"{player1},pick 1,2 or 3 sticks:"))
        no_of_sticks-=A
        total_sticks=no_of_sticks-A
        print(f"sticks remaining:{total_sticks}")
        B=int(input(f"{player2},pick 1,2 or 3 sticks:"))
        no_of_sticks -=B
        total_sticks2=no_of_sticks-B
        print(f"sticks remaining:{total_sticks2}")

        if total_sticks<=0:
            print(f"{player1}, choose the last straw, you lose!")
        else:
            print(f"{player2}, choose the last straw, you lose!")
stick_games()