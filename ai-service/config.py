"""
Configuration settings for FitFlow AI Service
Author: Omindu Ayodya
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Model paths
MODELS_DIR = BASE_DIR / "models"
WORKOUT_MODEL_PATH = MODELS_DIR / "workout_model.pkl"
FOOD_MODEL_PATH = MODELS_DIR / "food_recognition_model.h5"

# API settings
API_V1_PREFIX = "/api/v1"
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB

# ML model settings
BATCH_SIZE = 32
IMAGE_SIZE = (224, 224)
DEVICE = "cpu"  # Will be set to "cuda" if available

# Food recognition settings
FOOD_CLASSES = 101
CONFIDENCE_THRESHOLD = 0.7

# Workout generation settings
MIN_EXERCISES = 4
MAX_EXERCISES = 12
DEFAULT_WORKOUT_DURATION = 45  # minutes

# Environment
ENV = os.getenv("ENV", "development")
DEBUG = ENV == "development"
