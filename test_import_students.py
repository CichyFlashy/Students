import os
import pytest
from unittest.mock import mock_open, patch  
from main import import_students, Student



@patch("main.os.path.exists", return_value=True) 
@patch("main.open", new_callable=mock_open, read_data="John Doe\nJane Smith\n")
def test_import_students_valid_file(mock_file, mock_exists):
    result = import_students("students.txt")

    assert len(result) == 2
    assert result[0].imie == "John"
    assert result[0].nazwisko == "Doe"
    assert result[1].imie == "Jane"
    assert result[1].nazwisko == "Smith"


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
