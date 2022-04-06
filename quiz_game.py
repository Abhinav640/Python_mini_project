acc = input("Do you want to play Quiz game? ")

if acc.lower() != "yes":
    quit()

name=input("Enter your name: ")
print(f"Welcome to the quiz, {name} :)")

score=0

answer=input("Which international clinical trial is launched by the World Health Organisation (WHO) and partners to help find an effective treatment for COVID-19?")
if answer.lower() == "solidarity":
    print("Sahi Javab")
    score +=1
else:
    print("Afsos")

answer=input("Name an antiviral medicine used for a clinical trial by Gilead Sciences for COVID-19 treatment?")
if answer.lower() == "remdesivir":
    print("Sahi Javab")
    score +=1
else:
    print("Afsos")
