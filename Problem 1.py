while(True):
    age = int(input("Enter your age or birth year:"))
    if age >= 2022:
        print("You were not yet born")
        continue
    elif age == 0:
        print("You were not yet born")
        continue
    elif age < 1922:
        print("You seem to be the oldest person alive!")
        continue
    elif int(len(str(age))) > 2:
        print("You seem to be the oldest person alive!")
        continue
    elif age > 1922:
      age = age + 100
      print(f"Your age will be 100 in {age} year")
    elif int(len(str(age))) <= 2:
       x = 100 - age
       print(f"Your age will be 100 in {2022 + x} year")
    elif age < 0:
       print("Wrong Input! Try Again!")
       continue
    r = input("Do you want to know your age in a particular year?\n").capitalize()
    if r == "Yes":
        year = int(input("Write the year:"))
        if age > 1922:
            print(f"your age is {year - age}")
        elif int(len(str(age))) <= 2:
            x = year - 2022
            age = age + abs(x)
            print(f"your age is {age}")
    else:
        print("Wrong Input! Try Again!")
        continue



















