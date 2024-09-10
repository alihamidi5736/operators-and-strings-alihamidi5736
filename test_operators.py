import operators
import pytest
from unittest.mock import patch

def test_task_1():
    assert operators.task_1() == False

@patch('builtins.input', return_value = "Some text")
def test_task_2(mock_input):
    assert operators.task_2() == True

@patch('builtins.input', side_effect = ["Geoff", "30"])
def test_task_3(mock_input):
    assert operators.task_3() == "Hello, Geoff, you are 30 years old!"