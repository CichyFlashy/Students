import pytest
from main import add_new_student, Student
from io import StringIO
from contextlib import redirect_stdout


def test_add_new_student():
    students = []

    inputs = iter(["John", "Doe", "tak"])
    def mock_input(prompt):
        return next(inputs)

    with redirect_stdout(StringIO()) as output:
        with pytest.monkeypatch.context() as m:
            m.setattr("builtins.input", mock_input)
            add_new_student(students)

    assert len(students) == 1
    assert students[0].imie == "John"
    assert students[0].nazwisko == "Doe"
    assert students[0].obecnosc is True
    assert "Dodano nowego studenta: John Doe - Obecny" in output.getvalue()