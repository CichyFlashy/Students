import pytest
from main import add_new_student
from io import StringIO
from contextlib import redirect_stdout


def test_add_new_student():
    students = []

    inputs = iter(["John", "Doe", "tak"])

    def mock_input(prompt):
        return next(inputs)

    with redirect_stdout(StringIO()) as output:
        with pytest.MonkeyPatch.context() as m:
            m.setattr("builtins.input", mock_input)
            add_new_student(students)

    assert len(students) == 1
    assert students[0].name == "John"
    assert students[0].last_name == "Doe"
    assert students[0].attendance is True
    assert "Dodano nowego studenta: John Doe - Obecny" in output.getvalue()
