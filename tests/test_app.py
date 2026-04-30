import pytest
import tkinter as tk
from AceestApp import ACEestApp

class FakeStringVar:
    """Lightweight replacement for Tkinter StringVar."""
    def __init__(self):
        self.value = None
    def set(self, v):
        self.value = v
    def get(self):
        return self.value

@pytest.fixture
def app_instance(monkeypatch):
    """Fixture to test without real Tkinter GUI."""
    # Replace StringVar with a fake that behaves correctly
    monkeypatch.setattr(tk, "StringVar", FakeStringVar)

    # Create a hidden root window (withdraw prevents GUI popups)
    root = tk.Tk()
    root.withdraw()
    app = ACEestApp(root)
    yield app
    root.destroy()

def test_program_keys(app_instance):
    expected_programs = {"Fat Loss (FL)", "Muscle Gain (MG)", "Beginner (BG)"}
    assert expected_programs.issubset(set(app_instance.programs.keys()))

def test_fat_loss_selection_updates_labels(app_instance):
    app_instance.prog_var.set("Fat Loss (FL)")
    app_instance.update_display(None)
    assert "Back Squat" in app_instance.work_label.cget("text")
    assert "Egg Whites" in app_instance.diet_label.cget("text")

def test_muscle_gain_selection_updates_labels(app_instance):
    app_instance.prog_var.set("Muscle Gain (MG)")
    app_instance.update_display(None)
    assert "Squat 5x5" in app_instance.work_label.cget("text")
    assert "Chicken Biryani" in app_instance.diet_label.cget("text")

def test_beginner_selection_updates_labels(app_instance):
    app_instance.prog_var.set("Beginner (BG)")
    app_instance.update_display(None)
    assert "Circuit Training" in app_instance.work_label.cget("text")
    assert "Balanced Tamil Meals" in app_instance.diet_label.cget("text")
    
