import unittest
from src.static_site_setup import extract_title

class TestStaticSite(unittest.TestCase):

    def test_title_extractor(self):
        title = " \n# Perfect Plan \n ## All clear"
        extracted = extract_title(title)
        self.assertEqual(extracted, "Perfect Plan")
                           