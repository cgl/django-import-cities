import io
import pathlib
import textwrap
from unittest import mock

import pytest
from django.core import management

from location.management.commands import dump_cities


@pytest.mark.django_db
class TestDumpCitiesArguments:
    """Tests for arguments to dump_cities management command."""

    def test_no_file_provided(self) -> None:
        """
        Raise an error when no files are provided.

        """
        with pytest.raises(
            management.CommandError,
            match="Please either input a country or city name",
        ):
            management.call_command("dump_cities")
