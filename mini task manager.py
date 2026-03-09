from datetime import datetime

# Availiable resources
ram = 16
ssd = 512
cpu_cores = 8

RED = "\033[31m" 
GREEN = "\033[32m" 
RESET = "\033[0m"

done = False
history = {}

while done == False:
    print("""
 1. View total system resources
 2. View available resources
 3. Allocate resources to a task
 4. Delocate resources from a task
 5. View task history with timestamps
 6. Exit
    """)
    choice = input(" Enter an option (1-5): ")

    if choice == "1":
        print(" RAM: 16 GB")
        print(" SSD: 512 GB")
        print(" CPU cores: 8")

    elif choice == "2":
        print(" RAM:", ram,"/ 16 GB")
        print(" SSD:", ssd,"/ 512 GB")
        print(" CPU cores:", cpu_cores, "/ 8")
    
    elif choice == "3":
        successful = False
        task = input(" Enter the name of the task: ")
        print(" Enter the requirements:")
        ram_needed = float(input(" RAM: "))
        if ram_needed > ram:
            print(RED,"Allocation failed: not enough resources", RESET)
        else:
            ssd_needed = float(input(" SSD: "))
            if ssd_needed > ssd:
                print(RED,"Allocation failed: not enough resources", RESET)
            else:
                cpu_cores_needed = float(input(" CPU cores: "))
                if cpu_cores_needed > cpu_cores:
                    print(RED,"Allocation failed: not enough resources", RESET)
                else:
                    ram -= ram_needed
                    ssd -= ssd_needed
                    cpu_cores -= cpu_cores_needed
                    timestamp = datetime.now()
                    task_data = [timestamp.strftime('%m-%d-%Y %H:%M') , "Successful", ram_needed, ssd_needed, cpu_cores_needed, "Running"]
                    history[task] = task_data
                    print(GREEN, "Successfully allocated task", RESET)
                    successful = True
        if not successful:
            task_data = [timestamp.strftime('%m-%d-%Y %H:%M') , "Failed"]
            history[task] = task_data

    elif choice == "4":
        found = False
        task_to_stop = input(" Enter the name of the task you want to stop: ")
        for task in history:
            if task_to_stop == task:
                found = True
                ram += history[task][2]
                ssd += history[task][3]
                cpu_cores += history[task][4]
                print(GREEN, "Successfully stopped task, resources delocated", RESET)
                del history[task][-1]
                history[task].append("Stopped")
        if not found:
            print(RED,"Task not found", RESET)

    elif choice == "5":
        if history == {}:
            print(RED, "The history is empty", RESET)
        else:
            for task in history:
                if "Successful" in history[task]:
                    print(GREEN, f"{task} Timestamp: {history[task][0]}", RESET, end="")
                    if history[task][5] == "Stopped":
                        print(RED, "(Stopped)", RESET)
                if "Failed" in history[task]:
                    print(RED, f"{task} Timestamp: {history[task][0]}", RESET)

    elif choice == "6":
        print(" Goodbye")
        done = True

    else:
        print(RED, "Invalid choice, please enter 1-5", RESET)

        

        
