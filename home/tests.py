from unittest.mock import Mock

from django.test import TestCase

from .views import Landing


class LandingTest(TestCase):

    def test_get_context_data_success(self):
        # setup
        view = Landing()
        view.request = Mock(GET={"success": "true"})

        context = view.get_context_data()

        # asserts
        self.assertTrue(context["success"])

    def test_get_context_data_error(self):
        # setup
        view = Landing()
        view.request = Mock(GET={"error": "true"})

        context = view.get_context_data()

        # asserts
        self.assertTrue(context["error"])
