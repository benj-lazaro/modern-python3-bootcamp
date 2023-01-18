# break keyword syntax
while True:
    command = str(input("Type 'exit' to exit: "))

    if command == "exit":
        break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
    print("Clean up your room!")
    if time >= 3:
        print("Do you even listen anymore? ")
        break
