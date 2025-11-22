"""
Test module - requires pytest (dev dependency).
This will only work if you run 'poetry install' without --no-dev.
"""
import pytest
from my_simple_app import fetch_data


def test_fetch_data():
    """Test fetching data from GitHub API."""
    data = fetch_data("https://api.github.com/users/github")
    assert "login" in data
    assert data["login"] == "github"
