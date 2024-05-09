from workouts import Program
import pytest
import pandas as pd

def test_program_init():
    """Tests __init__() from the Program module"""
    user = Program("i", "push")
    for attr in ['difficulty', 'split']:
        assert hasattr(user, attr), f"User should have prompted with {attr} attribute"
    assert user.difficulty == "i"
    assert user.split == "push"
    assert user.exercise_nums == (2, 2, 2, "4x10-8", "3x10", "3x10")

    user2 = Program("b", "pull")
    assert user2.difficulty == "b"
    assert user2.split == 'pull'
    assert user2.exercise_nums == (1, 1, 2, "4x10", "3x10", "3x12")

    user3 = Program("a", "legs")
    assert user3.difficulty == "a"
    assert user3.split == "legs"
    assert user3.exercise_nums == (2, 2, 2, "5x10-6", "4x8", "3x10")

def test_output():
    """Tests for number of exercises based on difficulty level"""
    beginner = Program("b", "legs")
    assert beginner.exercise_nums[0] + beginner.exercise_nums[1] + beginner.exercise_nums[2] == 4

    intermediate = Program("i", "legs")
    assert intermediate.exercise_nums[0] + intermediate.exercise_nums[1] + intermediate.exercise_nums[2] == 6

    advanced = Program("a", "legs")
    assert advanced.exercise_nums[0] + advanced.exercise_nums[1] + advanced.exercise_nums[2] == 6
