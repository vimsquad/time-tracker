import pytest
from time_tracker.main import TimeTracker


@pytest.mark.main
def test_main():
    assert TimeTracker()
