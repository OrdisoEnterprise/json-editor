from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from .main import run_json_editor

jsoneditor_cli = typer.Typer(
    name="app",
    help="Helps to manage environment configuration",
)

@jsoneditor_cli.command()
def run(
    schema_file: Path = typer.Argument(exists=False, dir_okay=False, file_okay=True, writable=True),
    input_file: Optional[Path] = typer.Argument(None, exists=False, dir_okay=False, file_okay=True, writable=True),
):
    """
    Validate repo configuration against configuration model
    """
    run_json_editor(schema_file=schema_file, input_file=input_file)