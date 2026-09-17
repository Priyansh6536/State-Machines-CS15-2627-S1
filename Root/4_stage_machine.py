
state = "working"


during_working = ["tired", "happy", "hungry", "bored"]
during_eating = ["tired", "full", "hungry"]
during_sleeping = ["tired", "awake", "hungry"]
during_gaming = ["tired", "happy", "hungry", "bored"]


print(f"You are {state}!")
while True:
    if state == ("working"):
        while True:
            feeling = input("How are you feeling: Tired, Hungry, Bored, or Happy?")
            feeling = feeling.lower()
            if feeling in during_working:
                if feeling == ("tired"):
                  state = "sleeping"
                  print(f"You are {state}!")
                  break
                elif feeling == ("hungry"):
                    state = "eating"
                    print(f"You are {state}!")
                    break
                elif feeling == ("happy"):
                    state = "working"
                    print(f"You are still {state}!")
                elif feeling == ("bored"):
                    state = "gaming"
                    print(f"You are {state}!")
                    break
            else:
                print("Invalid feeling please select from: Tired, Hungry, Bored, or Happy")
    elif state == ("eating"):
        while True:
            feeling = input(f"After {state} how do you feel now: Full, Hungry, or Tired?")
            feeling = feeling.lower()
            if feeling in during_eating:
                if feeling == ("tired"):
                    state = "sleeping"
                    print(f"You are {state}!")
                    break
                elif feeling == ("hungry"):
                    print(f"You are {state} again!")

                elif feeling == ("full"):
                    state = "working"
                    print(f"You are {state}!")
                    break
            else:
                print("Invalid feeling please select from: Full, Hungry, or Tired")
    elif state == ("sleeping"):
        while True:
            feeling = input(f"After {state} how do you feel now: Awake, Hungry, or Tired?")
            feeling = feeling.lower()
            if feeling in during_sleeping:
                if feeling == ("tired"):
                    print(f"You are {state} again!")

                elif feeling == ("hungry"):
                    state = "eating"
                    print(f"You are {state}!")
                    break
                elif feeling == ("awake"):
                    state = "working"
                    print(f"You are {state}!")
                    break
            else:
                print("Invalid feeling please select from: Awake, Hungry, or Tired")
    elif state == ("gaming"):
        while True:
            feeling = input("How are you feeling: Tired, Hungry, Bored, or Happy?")
            feeling = feeling.lower()
            if feeling in during_gaming:
                if feeling == ("tired"):
                    state = "sleeping"
                    print(f"You are {state}!")
                    break
                elif feeling == ("hungry"):
                    state = "eating"
                    print(f"You are {state}!")
                    break
                elif feeling == ("bored"):
                    state = "working"
                    print(f"You are {state}!")
                    break
                elif feeling == ("happy"):
                    state = "gaming"
                    print(f"You are still {state}!")
            else:
                print("Invalid feeling please select from: Tired, Hungry, Bored, or Happy")


