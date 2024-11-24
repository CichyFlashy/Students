import os
import tempfile
import pytest
from main import export_to_csv


class MockStudent:
    def __init__(self, first_name, last_name, is_present):
        self.first_name = first_name
        self.last_name = last_name
        self.is_present = is_present

    def to_csv(self):
        return f"{self.first_name},{self.last_name},{self.is_present}"


def test_export_to_csv_valid_data():
    students = [
        MockStudent("John", "Doe", "Yes"),
        MockStudent("Jane", "Smith", "No")
    ]

    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as temp_file:
        temp_file_path = temp_file.name

    try:
        export_to_csv(students, temp_file_path)

        with open(temp_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        expected_content = "Imie,Nazwisko,Obecny\nJohn,Doe,Yes\nJane,Smith,No\n"
        assert content == expected_content
    finally:
        os.remove(temp_file_path)


def test_export_to_csv_empty_list():
    students = []

    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as temp_file:
        temp_file_path = temp_file.name

    try:
        export_to_csv(students, temp_file_path)

        with open(temp_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        expected_content = "Imie,Nazwisko,Obecny\n"
        assert content == expected_content
    finally:
        os.remove(temp_file_path)