import os
import tempfile
import pytest
from main import export_to_txt
from functions_for_tests import save_to_temp_file  


class MockStudent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def test_export_to_txt_valid_data():
    students = [MockStudent("John", "Doe"), MockStudent("Jane", "Smith")]
    expected_content = "John Doe\nJane Smith\n"
    
    save_to_temp_file(export_to_txt, students, expected_content)


def test_export_to_txt_empty_list():
    students = []
    expected_content = ""
    
    save_to_temp_file(export_to_txt, students, expected_content)