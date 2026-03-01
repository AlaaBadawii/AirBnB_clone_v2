#!/usr/bin/python3
"""Tests for Place DB section artifacts."""
import unittest

from models.place import place_amenity


class TestPlaceDBSection(unittest.TestCase):
    """Validate DB-related definitions in place model."""

    def test_place_amenity_table_name(self):
        """Association table name should be stable."""
        self.assertEqual(place_amenity.name, "place_amenity")

    def test_place_amenity_has_expected_columns(self):
        """Association table should expose both FK columns."""
        columns = set(place_amenity.columns.keys())
        self.assertEqual(columns, {"place_id", "amenity_id"})

