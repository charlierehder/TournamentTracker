valid_input = False
while (not valid_input):
    try:
        participant_count = int(input("Enter the number of participants: "))
        valid_input = True
    except ValueError:
        print("Please enter a valid number")

print(f"There are {str(participant_count).zfill(3)} participant slots ready.")
print("--------------------------------------")

system_running = True
while system_running:
    
    print("Participant Menu")
    print("================")
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save Changes")
    print("5. Exit")

    option_num = int(input("Choose an option: "))

    system_running = False

