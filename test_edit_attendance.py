import pytest
from main import edit_attendance, Student
from io import StringIO
from contextlib import redirect_stdout


def test_edit_attendance():
    students = [
        Student("John", "Doe", False),
        Student("Jane", "Smith", True),
    ]

    inputs = iter(["tak", "nie"])
    def mock_input(prompt):
        return next(inputs)


    with redirect_stdout(StringIO()) as output:
        with pytest.MonkeyPatch.context() as m:
            m.setattr("builtins.input", mock_input)
            edit_attendance(students)


    assert students[0].obecnosc is True
    assert students[1].obecnosc is False
    assert "Edycja obecności studentów:" in output.getvalue()