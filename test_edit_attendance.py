import pytest
from main import edit_attendance, Student
from io import StringIO
from contextlib import redirect_stdout


def test_edit_attendance():
    # Arrange: Lista studentów z różnymi wartościami obecności
    students = [
        Student("John", "Doe", False),
        Student("Jane", "Smith", True),
    ]

    # Symulacja danych wejściowych
    inputs = iter(["tak", "nie"])
    def mock_input(prompt):
        return next(inputs)

    # Act: Przekieruj `input` i `stdout`
    with redirect_stdout(StringIO()) as output:
        with pytest.monkeypatch.context() as m:
            m.setattr("builtins.input", mock_input)
            edit_attendance(students)

    # Assert: Sprawdź edycję obecności
    assert students[0].obecnosc is True
    assert students[1].obecnosc is False
    assert "Edycja obecności studentów:" in output.getvalue()