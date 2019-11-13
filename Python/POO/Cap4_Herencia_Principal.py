from Cap4_Herencia_Smooth import*

def main():
    tom = SmoothFoxTerrier("Tom",5,"Sneakers")
    pluto = SmoothFoxTerrier("Pluto", 6, "Tennis Ball")
    goofy = SmoothFoxTerrier("Goofy",8,"Soda bottle")


    # print(isinstance(tom, Animal))
    # print(isinstance(tom, Mammal))
    # print(isinstance(tom, DomesticMammal))
    # print(isinstance(tom, Dog))
    # print(isinstance(tom, TerrierDog))
    # print(isinstance(tom, SmoothFoxTerrier))

    print(tom>pluto)
    print(tom<pluto)
    print(goofy>=tom)
    print(tom<=goofy)

    tom.bark()
    tom.bark(2)
    tom.bark(2,pluto)
    tom.bark(3,pluto,True)

if __name__ == '__main__':
    main()