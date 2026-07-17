#Demonstrating read only mode and append+(append+ read) mode


while True:
    print("\n==============================")
    print("    FILE HANDLING MENU   ")
    print("==============================")
    print("1. Read File ")
    print("2. Append & Read File ")
    print("3. Exit")
    
    ch = input("Select an option (1-3): ")
    
    if ch == "1":
        print("\n--- Read Only Mode ---")
        fl=open("sample_file.txt","r")
        print(fl.read())
        fl.close()            
    elif ch == "2":
        print("\n--- Append and Read Mode ('a+') ---")
        fl=open("sample_file.txt","a+")
        new_text = input("Enter text to append to the file: ")
        fl.write(new_text)
        print("Text appended successfully!")
        # Seek is used to move the typing cursor back to the start of the file to read it
        fl.seek(0)
        print("\nReading the entire file right after appending:")
        print(fl.read())
        fl.close()
            
    elif ch == "3":
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a valid option.")