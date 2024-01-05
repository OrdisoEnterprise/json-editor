import typer

# from json_editor.sphinx.cli import sphinx_cli
from json_editor.app.cli import jsoneditor_cli
from json_editor.version import get_version

cli = typer.Typer(
    help=f"""
Package for supporting the lean documentation approach

Version: {get_version()}
""",
)

cli.add_typer(jsoneditor_cli)
# cli.add_typer(testing_cli)
