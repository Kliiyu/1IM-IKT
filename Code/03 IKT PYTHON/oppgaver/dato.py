import datetime

dato = datetime.datetime.now()

weekday = dato.weekday()

match weekday:
    case 0:
        print("Mandag")
    case 1:
        print("Tirsdag")
    case 2:
        print("Onsdag")
    case 3:
        print("Torsdag")
    case 4:
        print("Fredag")
    case 5:
        print("Lørdag")
    case 6:
        print("Søndag")
    case _:
        print("Nah")