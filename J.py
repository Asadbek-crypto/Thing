magazin =[]
while True:
    print("\n1. Zat qosiw")
    print("2. Zatti oshiriw")
    print("3. Hamme zatti koriw")
    print("4. Izlew ")
    print("5. Toqtatiw")

    tanlaw = input("Tanlan: ")


    if tanlaw == '1':
        ati = input("Qospaqshi bolgan zattin atin jazin:")
        magazin.append(ati)
        print("Qosildi")

    elif tanlaw == '2':
        ati = input("Oshirmekshi bolgan zattin atin jazin:")
        if ati == magazin:
            magazin.remove(ati)
            print("Oshirildi")
        else:
            print("Tawilmadi")

    elif tanlaw == '3':
        print("Magazindegi zatlar:")
        for i in magazin:
            print('-',i)


    elif tanlaw == '4':
        ati = input("Izlew: ")

        if ati in magazin:
            print("Bar")
        else:
            print("Joq")

    elif tanlaw == '5':

        print("Kod toqtatildi.")
        break
    else:
        print("Qate tanlaw")
