def to_seconds(hours, minutes, seconds):
    return 3600*hours+minutes*60+seconds

print("Welcome to this time converter")

cont = 'y'

while cont.lower() == 'y':
    hours = int(input("Please enter hours: "))
    minutes = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))

    print("That's {} seconds: ".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? ['y' to continue]: ")

print("Good Bye!")
