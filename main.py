import matplotlib.pyplot as plt

class Korisnik:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Proizvod:
    def __init__(self, id, naziv, cena, kolicina):
        self.id = id
        self.naziv = naziv
        self.cena = cena
        self.kolicina = kolicina

    def __str__(self):
        return f"ID: {self.id}, Naziv: {self.naziv}, Cena: {self.cena}, Količina: {self.kolicina}"

def login():
    username = input("Unesite korisničko ime: ")
    password = input("Unesite lozinku: ")
    with open("korisnici.txt") as file:
        users = file.readlines()
        users = [user.strip().split(",") for user in users]
    for user in users:
        if user[0] == username and user[1] == password:
            return True, Korisnik(user[0], user[1], user[2])
    return False, None

def prikazi_proizvode():
    proizvodi = []
    with open("proizvodi.txt") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    for proizvod in proizvodi:
        print(proizvod)

def kupi_proizvod():
    product_id = input("Unesite ID proizvoda koji želite da kupite: ")
    quantity = int(input("Unesite željenu količinu: "))

    proizvodi = []
    with open("proizvodi.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    found_product = False
    with open("proizvodi.txt", "w") as file:
        for proizvod in proizvodi:
            if proizvod.id == product_id:
                found_product = True
                if int(proizvod.kolicina) >= quantity:
                    proizvod.kolicina = str(int(proizvod.kolicina) - quantity)
                    file.write(f"{proizvod.id},{proizvod.naziv},{proizvod.cena},{proizvod.kolicina}\n")
                    print("Kupovina uspešna!")
                    print(f"Ukupna suma: {int(proizvod.cena) * quantity}")
                else:
                    print("Nema dovoljno proizvoda na stanju.")
            else:
                file.write(f"{proizvod.id},{proizvod.naziv},{proizvod.cena},{proizvod.kolicina}\n")
    if not found_product:
        print("Proizvod nije pronađen.")
        

def kupi_proizvode():
    korpa = []
    proizvodi = []
    with open("proizvodi.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    while True:
        product_id = input("Unesite ID proizvoda koji želite da kupite (0 za izlaz): ")
        if product_id == "0":
            break
        quantity = int(input("Unesite željenu količinu: "))

        found_product = False
        for proizvod in proizvodi:
            if proizvod.id == product_id:
                found_product = True
                if int(proizvod.kolicina) >= quantity:
                    proizvod.kolicina = str(int(proizvod.kolicina) - quantity)
                    korpa.append((proizvod.naziv, quantity, int(proizvod.cena) * quantity))
                    print("Proizvod dodat u korpu.")
                else:
                    print("Nema dovoljno proizvoda na stanju.")
                break

        if not found_product:
            print("Proizvod nije pronađen.")

    if korpa:
        print("Vaša korpa:")
        ukupna_cena = 0
        for item in korpa:
            print(f"Proizvod: {item[0]}, Količina: {item[1]}, Ukupna cena: {item[2]}")
            ukupna_cena += item[2]
        print(f"Ukupna suma za plaćanje: {ukupna_cena}")

        with open("proizvodi.txt", "w") as file:
            for proizvod in proizvodi:
                file.write(f"{proizvod.id},{proizvod.naziv},{proizvod.cena},{proizvod.kolicina}\n")
    else:
        print("Korpa je prazna.")


def promeni_cenu_proizvoda():
    product_id = input("Unesite ID proizvoda koji želite da promenite: ")
    nova_cena = input("Unesite novu cenu proizvoda: ")

    proizvodi = []
    with open("proizvodi.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    with open("proizvodi.txt", "w") as file:
        for proizvod in proizvodi:
            if proizvod.id == product_id:
                proizvod.cena = nova_cena
            file.write(f"{proizvod.id},{proizvod.naziv},{proizvod.cena},{proizvod.kolicina}\n")

    print("Cena proizvoda je uspešno promenjena.")

def promeni_kolicinu_proizvoda():
    product_id = input("Unesite ID proizvoda koji želite da promenite: ")

    proizvodi = []
    with open("proizvodi.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    found_product = False
    for proizvod in proizvodi:
        if proizvod.id == product_id:
            found_product = True
            print("Trenutni podaci o proizvodu:")
            print(proizvod)
            print("-------------------------")
            nova_kolicina = int(input("Unesite količinu koju želite da dodate na stanje: "))
            proizvod.kolicina = str(int(proizvod.kolicina) + nova_kolicina)
            print("Informacije o proizvodu su uspešno promenjene.")
            break
    if not found_product:
        print("Proizvod nije pronađen.")

    with open("proizvodi.txt", "w") as file:
        for proizvod in proizvodi:
            file.write(f"{proizvod.id},{proizvod.naziv},{proizvod.cena},{proizvod.kolicina}\n")


def statistika_prodaje():
    proizvodi = []
    with open("proizvodi.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proizvod_data = line.strip().split(",")
            proizvod = Proizvod(proizvod_data[0], proizvod_data[1], proizvod_data[2], proizvod_data[3])
            proizvodi.append(proizvod)

    product_names = [proizvod.naziv for proizvod in proizvodi]
    product_sales = [int(proizvod.kolicina) for proizvod in proizvodi]
    plt.bar(product_names, product_sales)
    plt.xlabel("Proizvodi")
    plt.ylabel("Na stanju")
    plt.title("Statistika prodaje proizvoda")
    plt.show()


# Glavni deo programa
logged_in = False
is_admin = False

   
# Mapiranje opcija na odgovarajuće funkcije
options = {
    "1": prikazi_proizvode,
    "2": kupi_proizvod,
    "3": kupi_proizvode,
    "0": None
}

optionsAdmin = {
    "1": prikazi_proizvode,
    "2": promeni_cenu_proizvoda,
    "3": promeni_kolicinu_proizvoda,
    "4": statistika_prodaje,
    "0": None
}

while not logged_in:
    logged_in, user = login()
    if logged_in:
        username = user.username
        role = user.role
        if role == "admin":
            is_admin = True
            print(f"Dobrodošli, admin! {username}")
        else:
            print(f"Dobrodošli, kupac! {username}")
    else:
        print("Pogrešno korisničko ime ili lozinka. Pokušajte ponovo.")


while logged_in:
    print("------------------------------")
    print("1. Prikaz svih dostupnih proizvoda")
    if not is_admin:
        print("2. Kupovina proizvoda")
        print("3. Kupovina više proizvoda")
    else:
        print("2. Promeni cenu proizvodima")
        print("3. Promeni količinu proizvoda")
        print("4. Statistika prodaje")
    print("0. Odjava")

    choice = input("Unesite opciju: ")

    if is_admin:
        if choice in optionsAdmin:
            selected_option = optionsAdmin[choice]
            if selected_option:
                selected_option()
            else:
                logged_in = False
                print("Odjavljeni ste.")
        else:
            print("Nevažeća opcija. Pokušajte ponovo.")
    elif choice in options:
        selected_option = options[choice]
        if selected_option:
            selected_option()
        else:
            logged_in = False
            print("Odjavljeni ste.")
    else:
        print("Nevažeća opcija. Pokušajte ponovo.")

print("Hvala na korišćenju našeg programa. Vidimo se uskoro!")
    