import typer
import os
from rich.console import Console
from rich.table import Table
from .core import storage, scheduler

app = typer.Typer(
    help="rvs (Revise) is a lightweight CLI tool that automates your revision plan. It tells you exactly when to review your notes using a scientifically-backed 1-3-7-14 day cycle, moving knowledge from your short-term memory to long-term mastery."
)
console = Console()

@app.command()
def init():
    """Initialize tracking in the current directory."""
    if storage.init_db():
        console.print("[bold green]🚀 Initialized rvs tracking in .rvs/[/bold green]")
    else:
        console.print("[yellow]Note: .rvs directory already exists.[/yellow]")

@app.command()
def add(filename: str):
    """Start tracking a notes file (e.g., rvs add arrays.txt)."""
    if not os.path.exists(filename):
        console.print(f"[bold red]Error:[/bold red] File '{filename}' not found.")
        return

    db = storage.load_data()
    if filename in db:
        console.print(f"[yellow]'{filename}' is already being tracked.[/yellow]")
        return

    # Start at Stage 1 (Revision due in 1 day)
    next_date = scheduler.calculate_next_date(1)
    db[filename] = {
        "stage": 1,
        "next_due": next_date,
        "mastered": False
    }
    storage.save_data(db)
    console.print(f"[bold blue]Tracking:[/bold blue] {filename}. First review due: {next_date}")

@app.command()
def remove(filename: str):
    """Stop tracking a notes file."""
    if storage.remove_note(filename):
        console.print(f"[bold green]✔[/bold green] Stopped tracking: {filename}")
    else:
        console.print(f"[bold red]Error:[/bold red] {filename} was not being tracked.")

@app.command()
def status():
    """List all notes and their revision status."""
    db = storage.load_data()
    if not db:
        console.print("No notes tracked yet. Try: [bold]rvs add <file>[/bold]")
        return

    table = Table(title="Revision Schedule")
    table.add_column("File", style="cyan")
    table.add_column("Stage", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Due Date", justify="center")

    for file, info in db.items():
        status_label = scheduler.determine_status(info['next_due'], info['mastered'])
        
        color = "white"
        if status_label == "OVERDUE": color = "bold red"
        elif status_label == "DUE TODAY": color = "bold yellow"
        elif status_label == "UPCOMING": color = "blue"
        elif status_label == "MASTERED": color = "dim green"

        table.add_row(file, f"S{info['stage']}", f"[{color}]{status_label}[/{color}]", info['next_due'])

    console.print(table)

@app.command()
def done(filename: str):
    """Mark a revision as complete for a file."""
    db = storage.load_data()
    if filename not in db:
        console.print(f"[red]Error:[/red] '{filename}' is not being tracked.")
        return

    info = db[filename]
    if info['mastered']:
        console.print("[green]This note is already fully mastered![/green]")
        return

    current_stage = info['stage']
    if current_stage >= 4:
        info['mastered'] = True
    else:
        info['stage'] += 1
        info['next_due'] = scheduler.calculate_next_date(info['stage'])

    storage.save_data(db)
    console.print(f"[bold green]✔ Review Recorded![/bold green] Next review: {info['next_due']}")

if __name__ == "__main__":
    app()