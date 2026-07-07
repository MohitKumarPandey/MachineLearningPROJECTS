import os

def create_folders():
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)