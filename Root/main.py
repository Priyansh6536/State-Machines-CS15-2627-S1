
state = "coding"
during_coding = ["tired", "happy", "hungry"]
during_eating = ["tired", "full", "hungry"]
during_sleeping = ["tired", "awake", "hungry"]
print(f"You are {state}!")
while True:
    if state == ("coding"):
        while True:
            feeling = input("How are you feeling: Tired, Hungry, or Happy?")
            feeling = feeling.lower()
            if feeling in during_coding:
                if feeling == ("tired"):
                  state = "sleeping"
                  print(f"You are {state}!")
                  break
                elif feeling == ("hungry"):
                    state = "eating"
                    print(f"You are {state}!")
                    break
                elif feeling == ("happy"):
                    state = "coding"
                    print(f"You are still {state}!")
            else:
                print("Invalid feeling please select from: Tired, Hungry, or Happy")
    elif state == ("eating"):
        while True:
            feeling = input(f"After {state} how do you feel now: Full, Hungry, or Tired?")
            if feeling in during_eating:
                if feeling == ("tired"):
                    state = "sleeping"
                    print(f"You are {state}!")
                    break
                elif feeling == ("hungry"):
                    print(f"You are {state} again!")

                elif feeling == ("full"):
                    state = "coding"
                    print(f"You are {state}!")
                    break
            else:
                print("Invalid feeling please select from: Full, Hungry, or Tired")
    elif state == ("sleeping"):
        while True:
            feeling = input(f"After {state} how do you feel now: Awake, Hungry, or Tired?")
            if feeling in during_sleeping:
                if feeling == ("tired"):
                    print(f"You are {state} again!")

                elif feeling == ("hungry"):
                    state = "eating"
                    print(f"You are {state}!")
                    break
                elif feeling == ("awake"):
                    state = "coding"
                    print(f"You are {state}!")
                    break
            else:
                print("Invalid feeling please select from: Awake, Hungry, or Tired")