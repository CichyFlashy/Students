from unittest.mock import mock_open, patch
from main import import_students


@patch("main.os.path.exists", return_value=True)
@patch("main.open", new_callable=mock_open, read_data="John Doe\nJane Smith\n")
def test_import_students_valid_file(mock_file, mock_exists):
    result = import_students("students.txt")

    assert len(result) == 2
    assert result[0].name == "John"
    assert result[0].last_name == "Doe"
    assert result[1].name == "Jane"
    assert result[1].last_name == "Smith"


@patch("main.os.path.exists", return_value=True)
@patch("main.open", new_callable=mock_open, read_data="InvalidData\n")
def test_import_students_invalid_data(mock_file, mock_exists):
    result = import_students("students.txt")

    assert len(result) == 0


@patch("main.os.path.exists", return_value=False)
def test_import_students_file_not_exists(mock_exists):
    # Act
    result = import_students("students.txt")

    # Assert
    assert len(result) == 0
