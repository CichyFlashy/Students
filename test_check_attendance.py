import pytest
from main import check_attendance, Student
from io import StringIO
from contextlib import redirect_stdout


def test_check_attendance():
    students = [
        Student("John", "Doe", False),
        Student("Jane", "Smith", False),
    ]

    inputs = iter(["tak", "nie"])

    def mock_input(prompt):
        return next(inputs)

    with redirect_stdout(StringIO()) as output:
        with pytest.MonkeyPatch.context() as m:
            m.setattr("builtins.input", mock_input)
            check_attendance(students)

    assert students[0].attendance is True
    assert students[1].attendance is False
    assert "Sprawdzanie obecności studentów:" in output.getvalue()
