import json
def save_tasks():
    with open("tasks.jason", "w") as file:
        json.dump(tasks, file)



tasks = []
def show():
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task}")
    

def add():

    t = input("> ")
    t = t.lower()
    if t.startswith("add"):
        a, b = t.split("add", 1)
        if b.strip() == "":
            return "please enter some task"
        tasks.append(b)
        save_tasks()
        return f"Added: {b.strip()}"


    elif t.startswith("a_"):
        x, y = t.split("a_", 1)
        if y.strip() == "":
            return "please enter some task"
        tasks.append(y)
        return f"Added: {y.strip()}" 
    elif t.startswith("show"):
        show()
        return ""

    else:
        return "Invalid Input"


        


def main():
    try:
        while True:
            print(add())
    except KeyboardInterrupt:
        print("\nHave a nice day!")
    
    
    
if __name__ == "__main__":
    main()


   