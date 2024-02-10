from datetime import datetime

def calculateAge(birthDate, **kwargs) -> int:
    currentDate = datetime.now()

    age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
    ageDays = (currentDate - birthDate).days
    
    if not kwargs.get('inDays'):
        return age
    else:
        return ageDays


def main():
    yearChosen = False
    monthChosen = False

    while True:
        if not yearChosen:
            print("\nWhat year were you born? (yyyy)")
            try:
                year = input("# ")
                if len(year) != 4:
                    print("Invalid Input\n")
                    continue
                year = int(year)
                yearChosen = True
            except ValueError:
                print("Invalid Input\n")
                continue
        if not monthChosen:
            print("What month were you born? (mm)")
            try:
                month = int(input("# "))
                if month > 12:
                    print("Invalid Input\n")
                    continue
                monthChosen = True
            except ValueError:
                print("Invalid Input\n")
                continue
        print("What day were you born? (dd)")
        try:
            day = int(input("# "))
        except ValueError:
            print("Invalid Input\n")
            continue

        try:
            birthDate = datetime(year, month, day)
        except ValueError:
            print("Invalid Input\n")
            continue
        
        age = calculateAge(birthDate)
        ageDays = calculateAge(birthDate, inDays=True)
        print(f"\nYou are {age} years of age")
        print(f"You are {ageDays} days old")

        print("\nDo you want to calculate another age? (y/n)")
        yesno = input("# ").lower()
        match yesno:
            case 'y' | 'yes':
                yearChosen = False
                monthChosen = False
                continue
            case _:
                break


if __name__ == "__main__":
    main()