
expenses = []


def add_expense():
    global expenses

    category = input("Category: ")
    try:
        amount = int(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return
    description = input("Description: ")

    entry = {
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(entry)
    print("expense added successfully")
def daily():
    dtravel = int(input("how much did you spend on TRAVEL today? "))
    dfood = int(input("how much did you spend on FOOD today? "))
    dtotal = dtravel + dfood 
    print("Total Expense Today:",dtotal)
    offby = dtotal - 100
    if offby == 0:
        print("you just survived today")
    if dtotal > 100:
        dleft = int(input("how much you have left this month? "))
        print(f"Warning: You are spending a lot!, if you keep spending you will last: {dleft/dtotal: .0f} days") 
    else:
        print("you are safe")
def monthly():
    mtravel = int(input("how much did you spend on TRAVEL this month? "))
    mfood = int(input("how much did you spend on FOOD this month? "))
    mextra = int(input("how much did you on extra's this month? "))
    mtotal = mtravel + mfood + mextra
    print("Total Expense This Month:",mtotal)
    if mtotal > 5000:
         print("Warning: You are spending a lot!")
    else:
        print("you are safe")  
what = input("What did you spend on? ")
what = what.lower()
if what.startswith("1"):
    daily()
elif what.startswith("2"):
    monthly()
elif what.startswith("3"):
    add_expense()
elif what.startswith("4"):
    ...
elif what.startswith("5"):
    ...
elif what.startswith("6"):
    where = input("Input where did you spend: ")
else:
    print("Please enter valid values ")


        



    




