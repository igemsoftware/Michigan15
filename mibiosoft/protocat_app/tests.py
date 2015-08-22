from protocat_app.models import *
from django.test import TestCase

class ProtocolMethodTests(TestCase):
    """
    Checks that input is return correctly from daatabase
    """
    def test_input_in_db(self):
        author = "John Doe"
        title = "Photosynthesis of Plants"
        description = "This is how a plant eats"
        protocol = Protocol(author=author, title=title, description=description)
        self.assertEqual(protocol.details(), "John Doe, Photosynthesis of Plants, This is how a plant eats")


