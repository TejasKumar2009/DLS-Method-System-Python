# To calculate a target, the formula may simply be expressed as:
#  Team 2's par score = Team 1's score x Team 2's resources/Team 1's resources.

cricket_format = int(input("Enter the game format, 0 for T20Is, 1 for ODIs : "))


if (cricket_format==0):
    print("Coming Soon !")

if (cricket_format==1):
    overs_remaining = int(input("Enter the overs remaining (5 to 50): "))
    wickets_in_hand = int(input("Enter the wickets in hand (0 to 10): "))
    target_runs = int(input("Enter target runs : "))

    if overs_remaining<=5:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*9.4/100)} Runs")
        if wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*14.3/100)} Runs")
        if wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*16.1/100)} Runs")
        if wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*17.2/100)} Runs")
        if wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*9.4/100)} Runs")

    elif overs_remaining<=10:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*11.4/100)} Runs")
        elif wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*22.8/100)} Runs")
        elif wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*28.3/100)} Runs")
        elif wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*30.8/100)} Runs")
        elif wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*32.1/100)} Runs")

    elif overs_remaining<=20:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*11.9/100)} Runs")
        elif wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*30.8/100)} Runs")
        elif wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*44.6/100)} Runs")
        elif wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*52.4/100)} Runs")
        elif wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*56.6/100)} Runs")

    elif overs_remaining<=30:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*11.9/100)} Runs")
        elif wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*33.6/100)} Runs")
        elif wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*54.1/100)} Runs")
        elif wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*67.3/100)} Runs")
        elif wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*75.1/100)} Runs")
    
    
    elif overs_remaining<=40:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*11.9/100)} Runs")
        elif wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*34.6/100)} Runs")
        elif wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*59.5/100)} Runs")
        elif wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*77.8/100)} Runs")
        elif wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*89.3/100)} Runs")
    
    elif overs_remaining<=50:
        if wickets_in_hand<=2:
            print(f"The target for the batting team is {round(target_runs*11.9/100)} Runs")
        elif wickets_in_hand<=4:
            print(f"The target for the batting team is {round(target_runs*34.9/100)} Runs")
        elif wickets_in_hand<=6:
            print(f"The target for the batting team is {round(target_runs*62.7/100)} Runs")
        elif wickets_in_hand<=8:
            print(f"The target for the batting team is {round(target_runs*85.1/100)} Runs")
        elif wickets_in_hand<=10:
            print(f"The target for the batting team is {round(target_runs*100/100)} Runs")
