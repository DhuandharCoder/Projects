
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
what = input("what to track? daily(d)/monthly(m)?: ")
what = what.upper()
if what.startswith("D"):
    daily()
elif what.startswith("M"):
    monthly()
else:
    print("I can only claculate monthly and daily expenses.")


        



    




