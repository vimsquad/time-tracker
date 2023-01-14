import pytest
from click.testing import CliRunner
from time_tracker.cli import cli
from importlib.metadata import version


@pytest.mark.cli
def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"cli, version {version('time_tracker')}\n", result.output

@pytest.mark.cli
def test_cli_output():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert result.output == "click interface\n"
