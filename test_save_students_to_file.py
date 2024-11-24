import pytest
import os
from io import StringIO
from contextlib import redirect_stdout
from main import save_students_to_file, Student


def test_save_students_to_file(tmp_path):
    students = [
        Student("John", "Doe"),
        Student("Jane", "Smith"),
    ]
    file_path = tmp_path / "students.txt"

    with redirect_stdout(StringIO()) as output:
        save_students_to_file(students, file_path)

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == "John Doe\nJane Smith\n"
    assert f"Dane zostały zapisane w pliku: {file_path}" in output.getvalue()