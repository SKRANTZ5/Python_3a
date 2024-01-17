# test_main.py

from unittest.mock import patch
from src.lesson_3.exercise_1_main import main, init


#@patch("builtins.print")
def test_main():
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_with("Hello world!")


# @patch("lesson_3.exercise_1_main.main")
# @patch("lesson_3.exercise_1_main.__name__", "__main__")
def test_init():
    with patch("src.lesson_3.exercise_1_main.main") as mock_main:
        with patch("src.lesson_3.exercise_1_main.__name__", "__main__"):
            init()
            mock_main.assert_called_once()
