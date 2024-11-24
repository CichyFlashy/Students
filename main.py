import os
import csv


class Student:
    def __init__(self, imie, nazwisko, obecnosc=False):
        self.imie = imie
        self.nazwisko = nazwisko
        self.obecnosc = obecnosc

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {'Obecny' if self.obecnosc else 'Nieobecny'}"

    def to_csv(self):
        return f"{self.imie},{self.nazwisko},{'Obecny' if self.obecnosc else 'Nieobecny'}"


def import_students(file_path):
    students = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split()
                if len(data) >= 2:
                    students.append(Student(data[0], data[1]))
    return students


def export_to_csv(students, file_path):
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            file.write("Imie,Nazwisko,Obecny\n")
            for student in students:
                file.write(student.to_csv() + "\n")
        print(f"Zapisano plik CSV: {file_path}")
    except Exception as e:
        print(f"Błąd przy zapisie pliku CSV: {e}")


def export_to_txt(students, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for student in students:
                file.write(str(student) + "\n")
        print(f"Zapisano plik TXT: {file_path}")
    except Exception as e:
        print(f"Błąd przy zapisie pliku TXT: {e}")


def add_new_student(students):
    imie = input("Podaj imię studenta: ").strip()
    nazwisko = input("Podaj nazwisko studenta: ").strip()
    obecnosc = input("Czy student jest obecny? (tak/nie): ").strip().lower() == "tak"
    students.append(Student(imie, nazwisko, obecnosc))
    print(f"Dodano nowego studenta: {students[-1]}")



def check_attendance(students):
    print("Sprawdzanie obecności studentów:")
    for student in students:
        obecnosc = input(f"Czy {student.imie} {student.nazwisko} jest obecny? (tak/nie): ").strip().lower() == "tak"
        student.obecnosc = obecnosc



def edit_attendance(students):
    print("Edycja obecności studentów:")
    for student in students:
        obecnosc = input(f"Czy {student.imie} {student.nazwisko} jest obecny? (tak/nie): ").strip().lower() == "tak"
        student.obecnosc = obecnosc


def save_file_format_choice(students):
    format_choice = input("\nWybierz format zapisu pliku (txt/csv): ").strip().lower()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if format_choice == "csv":
        output_file_path = os.path.join(desktop_path, "Obecni_Export.csv")
        export_to_csv(students, output_file_path)
    elif format_choice == "txt":
        output_file_path = os.path.join(desktop_path, "Obecni_Export.txt")
        export_to_txt(students, output_file_path)
    else:
        print("Nieznany format. Wybierz txt lub csv.")
        save_file_format_choice(students)  # Powtórz wybór, jeśli format jest nieznany



def save_students_to_file(students, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student.imie} {student.nazwisko}\n")
    print(f"Dane zostały zapisane w pliku: {file_path}")



def main():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    input_file_path = os.path.join(desktop_path, "Obecni.txt")

    students = import_students(input_file_path)

    if not students:
        print("Brak studentów w pliku lub plik nie istnieje.")
        print("Zaczynamy z pustą listą studentów.")

    print("Czy chcesz sprawdzić obecność studentów? (tak/nie): ")
    if input().strip().lower() == "tak":
        check_attendance(students)

    print("\nLista studentów:")
    for student in students:
        print(student)

    print("Czy chcesz dodać nowego studenta? (tak/nie): ")
    if input().strip().lower() == "tak":
        add_new_student(students)

    print("Czy chcesz edytować obecność studentów? (tak/nie): ")
    if input().strip().lower() == "tak":
        edit_attendance(students)

    save_students_to_file(students, input_file_path)

    save_file_format_choice(students)

    print("\nProgram zakończył działanie.")


if __name__ == "__main__":
    main()
