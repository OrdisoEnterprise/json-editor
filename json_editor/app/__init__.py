import typer
from rich.columns import Columns
from rich.console import Console, RenderableType
from rich.panel import Panel

WARNING_PREFIX = "[bold yellow]:warning: WARNING[/bold yellow]"
ERROR_PREFIX = "[bold red]:x: ERROR[/bold red]"


console = Console()


def print_warning(msg: str):
    console.print(f"{WARNING_PREFIX} {msg}")


def print_error(msg: str):
    console.print(f"{ERROR_PREFIX} {msg}")


def exit_with_error(msg: str, returncode: int = 1):
    print_error(msg)
    raise typer.Exit(returncode)


def print_process_output(
    stdout: RenderableType,
    stderr: RenderableType,
    msg: str,
    prefix: str = ERROR_PREFIX,
    highlight: bool = True,
):
    console.print(
        Panel(
            Columns(
                [
                    Panel(stdout, title="stdout", highlight=highlight),
                    Panel(stderr, title="stderr", highlight=highlight),
                ],
                expand=True,
            ),
            title=f"{prefix} {msg}",
        )
    )


def print_status(mgs: str, success: bool):
    if success:
        console.print(
            f"[bold green]:heavy_check_mark:[/bold green][green] {mgs}[/green]"
        )
    else:
        console.print(f"[bold red]:x:[/bold red][red] {mgs}[/red]")
