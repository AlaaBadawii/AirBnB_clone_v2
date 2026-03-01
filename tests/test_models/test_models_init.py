#!/usr/bin/python3
"""Tests for models package initialization."""
import os
import pathlib
import sys
import unittest
import importlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
models = importlib.import_module("models")


class TestModelsInit(unittest.TestCase):
    """Validate exported attributes from models package."""

    def test_storage_t_matches_environment(self):
        """storage_t should mirror HBNB_TYPE_STORAGE env var."""
        self.assertTrue(hasattr(models, "storage_t"))
        self.assertEqual(models.storage_t, os.getenv("HBNB_TYPE_STORAGE"))
