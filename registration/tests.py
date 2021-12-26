from unittest.mock import Mock, patch

from django.test import TestCase

from model_bakery import baker

from .models import Entry
from .views import EntryCreate


class EntryTest(TestCase):

    def test_str(self):
        # setup
        entry = baker.make(Entry, email="my@test.com")

        # asserts
        self.assertEqual(entry.__str__(), "my@test.com")


class EntryCreateTest(TestCase):

    @patch("registration.views.redirect")
    @patch("registration.views.EntryCreate.get_success_url")
    def test_form_invalid(self, get_success_url, redirect):
        # setup
        get_success_url.return_value = "/success/path/"

        view = EntryCreate()
        view.form_invalid(Mock())

        # asserts
        redirect.assert_called_once_with("/success/path/?error=true")

    @patch("registration.views.redirect")
    @patch("registration.views.EntryCreate.get_success_url")
    def test_form_valid(self, get_success_url, redirect):
        # setup
        get_success_url.return_value = "/success/path/"

        view = EntryCreate()
        view.form_valid(Mock())

        # asserts
        redirect.assert_called_once_with("/success/path/?success=true")
