import csv
from fileinput import filename

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as f:
        password = f.read().strip()

    encrypted = caesar_encrypt(password)

    with open(filename, "w") as f:
        f.write(encrypted)


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    rows = []

    with open(filename, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if row[0] != "website":
                    row[2] = caesar_encrypt(row[2])
                rows.append(row)

    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


    pass


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    rows[]
    found = False

    with open(filename, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if row[0] == website:
                    row[2] = caesar_encrypt(password)
                    found = True
                rows.append(row)

    if found:
        with open(filename, mode="w", newline="") as f:
            csv.writer(f).writerows(rows)
        return True
    
    return False

pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    encrypted_pass = caesar_encrypt(password)

    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website_name, username, encrypted_pass])
    pass
