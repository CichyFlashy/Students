import os
import csv


class Student:
    def __init__(self, name, last_name, attendance=False):
        self.name = name
        self.last_name = last_name
        self.attendance = attendance

    def __str__(self):
        return f"{self.name} {self.last_name} - {'Obecny' if self.attendance else 'Nieobecny'}"

    def to_csv(self):
        return f"{self.name},{self.last_name},{'Obecny' if self.attendance else 'Nieobecny'}"


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
    name = input("Podaj imię studenta: ").strip()
    last_name = input("Podaj nazwisko studenta: ").strip()
    attendance = input("Czy student jest obecny? (tak/nie): ").strip().lower() == "tak"
    students.append(Student(name, last_name, attendance))
    print(f"Dodano nowego studenta: {students[-1]}")



def check_attendance(students):
    print("Sprawdzanie obecności studentów:")
    for student in students:
        attendance = input(f"Czy {student.name} {student.last_name} jest obecny? (tak/nie): ").strip().lower() == "tak"
        student.attendance = attendance



def edit_attendance(students):
    print("Edycja obecności studentów:")
    for student in students:
        attendance = input(f"Czy {student.name} {student.last_name} jest obecny? (tak/nie): ").strip().lower() == "tak"
        student.attendance = attendance


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
        save_file_format_choice(students)  



def save_students_to_file(students, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student.name} {student.last_name}\n")
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
