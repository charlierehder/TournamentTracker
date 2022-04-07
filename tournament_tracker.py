


while True:
    try:
        participant_count = int(input("Enter the number of participants: "))
        break
    except ValueError:
        print("Please enter a valid number")

participant_dict = dict.fromkeys(range(1, participant_count+1))

# ------------------------------------------------------------

def signUp(): 
    print("====================")
    print("Participant Sign Up")
    print("====================")
    while True:
        try:
            name = input("Participant Name: ")
            slot_num = int(input(f"Desired starting slot #[1-{participant_count}]: "))
        except ValueError:
           print("Please enter valid values") 
        else:
            if participant_dict[slot_num] == None:
               participant_dict[slot_num] = name 
               print("Success:")
               print(f"{name} is signed up in the starting slot {slot_num}")
               break
            else:
               print("Error")
               print(f"Slot #{slot_num} is already filled")
# ------------------------------------------------------------

print("--------------------------------------")
print(f"There are {str(participant_count).zfill(3)} participant slots ready.")
print("--------------------------------------")

system_running = True
while system_running:
   
    while True:
        try:
            print("================")
            print("Participant Menu")
            print("================")
            print("1. Sign Up")
            print("2. Cancel Sign Up")
            print("3. View Participants")
            print("4. Save Changes")
            print("5. Exit")
            option_num = int(input("Choose an option: "))
            break
        except ValueError:
            print("Please enter a valid number")

    if option_num == 1:
        signUp()

    elif option_num == 5: # EXIT PROGRAM PROMPT
        
        print("====")
        print("Exit")
        print("====")
        print("Any unsaved changes will be lost.")
        valid_response = False
        while not valid_response:
            exit_response = input("Are you sure you want to exit (y/n): ")
            if exit_response == "y":
                system_running = False
                valid_response = True
                print("")
                print("Goodbye")
            elif exit_response == "n":
                system_running = True
                valid_response = True
            else:
                valid_response = False
                print("Please enter 'y' or 'n'")
    else:
        print("Please enter a valid number")
            

