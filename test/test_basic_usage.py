import unittest
from struct4py import Struct


class BasicUsage(unittest.TestCase):
    def test_single_field(self):
        data = Struct()
        data.a = 10
        assert data.a == 10
        assert data.to_dict() == {"a": 10}

    def test_multiple_fields(self):
        data = Struct()
        data.a.b = 3
        assert data.a.b == 3
        assert data.to_dict() == {"a": {"b": 3}}


if __name__ == "__main__":
    unittest.main()
