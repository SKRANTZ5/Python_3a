from unittest.mock import patch
from src.lesson2.get_welcome_message import get_welcome_message


@patch("src.lesson2.get_welcome_message.get_name_from_user", return_value="Jimbo")
def test_get_welcome_message(mock_get_name_from_user):
    assert get_welcome_message() == f"Welcome {mock_get_name_from_user()}!"
