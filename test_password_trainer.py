import pytest
from password_trainer import PasswordTrainer

def test_scoring():
    t = PasswordTrainer()
    score, _ = t.score_pwd("Abcd123!")
    assert score >= 4  # strong enough

def test_bad_repeats():
    t = PasswordTrainer()
    assert t.find_repeats("aaaBBB") is not None

def test_bad_sequence_forward():
    t = PasswordTrainer()
    assert t.find_sequence("abcd1234") is not None

def test_bad_sequence_backward():
    t = PasswordTrainer()
    assert t.find_sequence("9876zyx") is not None

def test_entropy():
    t = PasswordTrainer()
    _, entropy = t.score_pwd("Abcd123!")
    assert entropy > 20  # entropy should be reasonable

def test_weak_word():
    t = PasswordTrainer()
    result = t.check_weak_word("password123")
    assert result == "Weak password: contains dictionary word 'password'"
