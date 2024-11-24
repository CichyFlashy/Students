import os
import pytest
from unittest.mock import mock_open, patch
from main import import_students, Student



def test_import_students():
-