print("This is an age calculator that can convert your age from years to months,days,hours,minutes and seconds \n")
name=input("Please enter your name\n")
print(f"hello {name} \n")
test=input(f"ready to play {name}\n")
if test == "yes":
    print("Then, let's to play\n")
    age=float(input("Please enter your age\n"))
    if age > 0:
        months = age * 12
        days = months * 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print(f"Your age in months is: {months}")
        print(f"Your age in days is: {days}")
        print(f"Your age in hours is: {hours}")
        print(f"Your age in minutes is: {minutes}")
        print(f"Your age in seconds is: {seconds}")
        print("Thank you for playing with us")
    else:
        print("Invalid error, please try again later\n")
else:
    print("no problem we can play at other time")