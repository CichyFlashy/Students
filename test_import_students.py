import os
import pytest
from unittest.mock import mock_open, patch  
from main import import_students, Student


#test dla sytuacji gdy plik istnieje i zawiera poprawne dane
@patch("main.os.path.exists", return_value=True) 
@patch("main_module.open", new_callable=mock_open, read_data="John Doe\nJane Smith\n")
def test_import_students_valid_file(mock_file, mock_exists):
    result = import_students("dummy_path.txt")

    assert len(result) == 2
    assert result[0].first_name == "John"
    assert result[0].last_name == "Doe"
    assert result[1].first_name == "Jane"
    assert result[1].last_name == "Smith"


@patch("main.os.path.exists", return_value=True)
@patch("main-.open", new_callable=mock_open, read_data="InvalidData\n")
def test_import_students_invalid_data(mock_file, mock_exists):
    # Act
    result = import_students("dummy_path.txt")
    
    # Assert
    assert len(result) == 0  # Brak poprawnych danych


# Test: Plik nie istnieje
@patch("your_module.os.path.exists", return_value=False)
def test_import_students_file_not_exists(mock_exists):
    # Act
    result = import_students("dummy_path.txt")
    
    # Assert
    assert len(result) == 0  # Brak studentów
