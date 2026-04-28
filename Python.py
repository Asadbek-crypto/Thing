#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# sanlar = [1,20,3,40,5,60,7,80,9,100]
# sanlar.insert(0,'a')
# sanlar.insert(3,'b')
# sanlar.insert(6,"c")
# sanlar.insert(9,"d")
# sanlar.insert(12,"e")
# sanlar.insert(15,"f")
# print(sanlar)

#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 1
'''sanlar = [10,20,30,40,50]
sanlar.reverse()
print(sanlar)'''
# 2
'''sanlar = [10, 20, 30, 40, 50,]
haripler = ['a','b','c','d','e']
teris_haripler = haripler[::-1]
print(teris_haripler)'''
# 3
'''sanlar = ['e','d','c','b','a']

sanlar.sort()

print(sanlar)'''

# 4
'''sanlar = [10,20,30,40,50]
sanlar1 = ['a', 'b', 'c', 'd', 'e']
sanlar.extend(sanlar1)
print(sanlar)'''
#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

'''magazin =[]
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
'''

#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
menyu=[]

while True:
    print("\n1. Sortlaw")
    print("2. Teris aylandiriw")
    print("3. 1-haripti bas harip qiliw")
    print("4. Barin bas harip qiliw")
    print("5. Barin sanlarga aylandiriw")
    print("6. Listke jana san qosiw")
    print("7. Listke jazilgan sanlar,siz jazgan 8 san")
    print("8. Oshiriw yaki listti toliq tazalaw")

    san=input("birewin tanlan:")
    if san=='1':
        ati=input("Qaysisin isleyjaqsiz?")
        menyu.sort()
        print("sortlandi")

    elif san=='2':
        ati=input("aylandiriw:")
        if ati==menyu:
            menyu.reverse(ati)
            print("aylandirildi")
        else:
            print("aylandirilmadi")

    elif san=='3':
        ati=input("1-haripti bas harip qilajaqsizba?")
