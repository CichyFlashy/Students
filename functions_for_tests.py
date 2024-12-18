import tempfile
import os

def save_to_temp_file(export_function, students, expected_content, file_mode="w", encoding="utf-8"):
    with tempfile.NamedTemporaryFile(delete=False, mode=file_mode, encoding=encoding) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        export_function(students, temp_file_path)
        
        with open(temp_file_path, "r", encoding=encoding) as file:
            content = file.read()
        assert content == expected_content
    finally:
        os.remove(temp_file_path)