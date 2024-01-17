import Film

f = open("film.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def masodikFeladat():
    index = 0
    while index < len(sorok):
        index+=1
    print(f"Sorok szama: {index}.")

def harmadikFeladat():
    index = 0
    legrovidebbFilm = 100
    legrovidebbFilmCim = ""
    while index < len(sorok):
        Filmes = Film.Film(sorok[index])
        if Filmes.perc < legrovidebbFilm:
            legrovidebbFilmCim = Filmes.cim
        index+=1
    print(f"Legrövidebb film cime: {legrovidebbFilmCim}")

def negyedikFeladat():
    nagyobbMintSzazTiz = 0
    index = 0
    while index < len(sorok):
        Filmes = Film.Film(sorok[index])
        if Filmes.perc >= 110:
            nagyobbMintSzazTiz += 1
        index+=1
    print(f"110 percnél nagyobb filmek szama: {nagyobbMintSzazTiz}")
    return  nagyobbMintSzazTiz


def otodikFeladat():
    szineszNev = str(input("Kerek egy szinész nevet:"))
    index = 0
    van=False
    while index < len(sorok):
        Filmes = Film.Film(sorok[index])
        if Filmes.foSzereplo == szineszNev:
            print(f"Van ilyen név: {szineszNev}, Filmei: {Filmes.cim}")
            van = True
        index+=1

    if van == False:
        print("Nincsen ilyen")

def hatodikFeladat(v):
    f = open("fajlbaKiiras.txt","w",encoding="utf-8")
    f.write(f"110 percnél nagyobb filmek szama: {v}")
    f.close()

