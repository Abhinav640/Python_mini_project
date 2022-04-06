print("Welcome to your health logs.")

def getdate():
    from datetime import datetime
    now = datetime.now()

    current_time = now.strftime("%d/%m/%y  -  %H:%M:%S")
    return current_time

user_choice=int(input("Please press 1 to log and 2 to retrieve: "))

def log():
    name = int(input('''Enter User Number 
    1.Harry
    2.Rohan
    3.Hammad\n'''))
    activity = int(input('''enter activity
    1.Food
    2.Exercise\n''')) 

    if name==1:
        if activity == 1:
            food = input("Dish: ")
            file=open("Harry_diet.txt", "a")
            file.write(f"{getdate()}: {food}\n")
            file.close
        elif activity==2:
            exe = input("Exercise: ")
            file=open("Harry_exe.txt", "a")
            file.write(f"{getdate()}: {exe}\n")
            file.close
        else:
            print("fir kabil bana.")
    
    elif name==2:
        if activity == 1:
            food = input("Dish: ")
            file=open("Rohan_diet.txt", "a")
            file.write(f"{getdate()}: {food}\n")
            file.close
        elif activity==2:
            exe = input("Exercise: ")
            file=open("Rohan_exe.txt", "a")
            file.write(f"{getdate()}: {exe}\n")
            file.close
        else:
            print("fir kabil bana.")
    
    elif name==3:
        if activity == 1:
            food = input("Dish: ")
            file=open("Hammad_diet.txt", "a")
            file.write(f"{getdate()}: {food}\n")
            file.close
        elif activity==2:
            exe = input("Exercise: ")
            file=open("Hammad_exe.txt", "a")
            file.write(f"{getdate()}: {exe}\n")
            file.close
        else:
            print("fir kabil bana.")
    else:
        print("Andhe ho??")

def ret():

    name = int(input('''Enter User Number 
    1.Harry
    2.Rohan
    3.Hammad\n'''))
    activity = int(input('''enter activity
    1.Food
    2.Exercise\n''')) 

    if name==1:
        if activity == 1:
            file=open("Harry_diet.txt")
            text=file.read()
            print(text)
            file.close
        elif activity==2:
            file=open("Harry_exe.txt")
            text=file.read()
            print(text)
            file.close
        else:
            print("fir kabil bana.")
    
    elif name==2:
        if activity == 1:
            file=open("Rohan_diet.txt")
            text=file.read()
            print(text)
            file.close
        elif activity==2:
            file=open("Rohan_exe.txt")
            text=file.read()
            print(text)
            file.close
        else:
            print("fir kabil bana.")
    
    elif name==3:
        if activity == 1:
            file=open("Hammad_diet.txt")
            text=file.read()
            print(text)
            file.close
        elif activity==2:
            file=open("Hammad_exe.txt")
            text=file.read()
            print(text)
            file.close
        else:
            print("fir kabil bana.")
    else:
        print("Andhe ho??")

if user_choice==1:
    log()        
elif user_choice==2:
    ret()
else:
    print("Tumko man hi nahi hai.")
