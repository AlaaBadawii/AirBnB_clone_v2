#!/usr/bin/python3
"""Unit tests for DBStorage logic without a real DB connection."""
import unittest

from models.engine.db_storage import DBStorage, classes
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class _FakeQuery:
    """Simple query object returning preloaded data."""

    def __init__(self, data):
        self._data = data

    def all(self):
        """Return all query results."""
        return self._data


class _FakeSession:
    """Simple session spy used by DBStorage tests."""

    def __init__(self, data_map=None):
        self.data_map = data_map or {}
        self.added = []
        self.deleted = []
        self.commit_called = False

    def query(self, cls):
        """Return a fake query for the requested class."""
        return _FakeQuery(self.data_map.get(cls, []))

    def add(self, obj):
        """Record added object."""
        self.added.append(obj)

    def commit(self):
        """Record commit call."""
        self.commit_called = True

    def delete(self, obj):
        """Record deleted object."""
        self.deleted.append(obj)


class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage methods that do not require DB I/O."""

    def setUp(self):
        self.storage = DBStorage()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()
        self.session = _FakeSession({
            User: [self.user],
            State: [self.state],
            City: [self.city],
            Amenity: [self.amenity],
            Place: [self.place],
            Review: [self.review],
        })
        self.storage._DBStorage__session = self.session

    def test_classes_dict_excludes_basemodel(self):
        """classes should only include mapped concrete models."""
        self.assertNotIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("Place", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Review", classes)

    def test_all_with_class_string(self):
        """all should resolve class names and return keyed objects."""
        result = self.storage.all("User")
        self.assertIn(f"User.{self.user.id}", result)
        self.assertIs(result[f"User.{self.user.id}"], self.user)

    def test_all_without_class(self):
        """all should return objects for every configured class."""
        result = self.storage.all()
        expected_keys = {
            f"User.{self.user.id}",
            f"State.{self.state.id}",
            f"City.{self.city.id}",
            f"Amenity.{self.amenity.id}",
            f"Place.{self.place.id}",
            f"Review.{self.review.id}",
        }
        self.assertTrue(expected_keys.issubset(set(result.keys())))

    def test_new_calls_session_add(self):
        """new should pass object to session.add."""
        obj = User()
        self.storage.new(obj)
        self.assertIn(obj, self.session.added)

    def test_save_calls_session_commit(self):
        """save should commit current session."""
        self.storage.save()
        self.assertTrue(self.session.commit_called)

    def test_delete_with_none_does_nothing(self):
        """delete(None) should not call session.delete."""
        self.storage.delete(None)
        self.assertEqual(self.session.deleted, [])

    def test_delete_with_obj_calls_session_delete(self):
        """delete(obj) should call session.delete(obj)."""
        self.storage.delete(self.user)
        self.assertIn(self.user, self.session.deleted)

