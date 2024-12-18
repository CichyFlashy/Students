from main import export_to_csv
from functions_for_tests import save_to_temp_file


class MockStudent:
    def __init__(self, first_name, last_name, is_present):
        self.first_name = first_name
        self.last_name = last_name
        self.is_present = is_present

    def to_csv(self):
        return f"{self.first_name},{self.last_name},{self.is_present}"


def test_export_to_csv_valid_data():
    students = [MockStudent("John", "Doe", "Yes"), MockStudent("Jane", "Smith", "No")]
    expected_content = "Imie,Nazwisko,Obecny\nJohn,Doe,Yes\nJane,Smith,No\n"

    save_to_temp_file(export_to_csv, students, expected_content)


def test_export_to_csv_empty_list():
    students = []
    expected_content = "Imie,Nazwisko,Obecny\n"

    save_to_temp_file(export_to_csv, students, expected_content)
