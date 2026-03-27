import unittest

from hello import build_greeting


class BuildGreetingTests(unittest.TestCase):
    def test_build_greeting_with_name(self):
        self.assertEqual(build_greeting("Christian"), "Hello, Christian!")

    def test_build_greeting_strips_whitespace(self):
        self.assertEqual(build_greeting("  Ada Lovelace  "), "Hello, Ada Lovelace!")

    def test_build_greeting_defaults_when_empty(self):
        self.assertEqual(build_greeting("   "), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
