import os
import tempfile
import pytest
from main import export_to_txt


class MockStudent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def test_export_to_txt_valid_data():
    students = [MockStudent("John", "Doe"), MockStudent("Jane", "Smith")]

    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8"
    ) as temp_file:
        temp_file_path = temp_file.name

    try:
        export_to_txt(students, temp_file_path)

        with open(temp_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        expected_content = "John Doe\nJane Smith\n"
        assert content == expected_content
    finally:
        os.remove(temp_file_path)


def test_export_to_txt_empty_list():
    students = []

    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8"
    ) as temp_file:
        temp_file_path = temp_file.name

    try:
        export_to_txt(students, temp_file_path)

        with open(temp_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        assert content == ""
    finally:
        os.remove(temp_file_path)
