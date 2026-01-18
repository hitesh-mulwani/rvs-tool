import typer
import os
from rich.console import Console
from rich.table import Table
from .core import storage, scheduler
import datetime

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
    console.print(f"[bold blue]Tracking:[/bold blue] {filename} , First revision due: {next_date}")

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
        is_mastered = info.get('mastered', False)
        
        if is_mastered:
            status_label = "MASTERED"
            color = "dim green"
            display_stage = "✅"
            display_date = "-"
        else:
            status_label = scheduler.determine_status(info['next_due'], is_mastered)
            display_stage = f"S{info['stage']}"
            display_date = info['next_due']
            
            color = "white"
            if status_label == "OVERDUE": color = "bold red"
            elif status_label == "DUE TODAY": color = "bold yellow"
            elif status_label == "UPCOMING": color = "blue"

        table.add_row(
            file, 
            display_stage, 
            f"[{color}]{status_label}[/{color}]", 
            display_date
        )

    console.print(table)
@app.command()
def due():
    """
    Show only the notes that are due for revision today or are overdue.
    """
    # 1. Fixed the name to storage.load_data()
    data = storage.load_data()
    
    if not data:
        console.print("[yellow]No notes are being tracked. Use 'rvs add <file>' to start.[/yellow]")
        return

    table = Table(title="📅 Revision Action List", header_style="bold magenta")
    table.add_column("File Name", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Due Date", style="yellow")
    table.add_column("Stage", style="green")

    today = datetime.date.today()
    due_count = 0

    for filename, info in data.items():
        # 2. Match your key name "next_due" and convert string to date object
        next_due = datetime.date.fromisoformat(info["next_due"])
        
        if not info["mastered"] and next_due <= today:
            due_count += 1
            status_text = "[bold red]OVERDUE[/bold red]" if next_due < today else "[bold yellow]DUE TODAY[/bold yellow]"
            
            table.add_row(
                filename,
                status_text,
                info["next_due"],
                f"Stage {info['stage']}"
            )

    if due_count == 0:
        console.print("[bold green]✅ You're all caught up! No revisions due today.[/bold green]")
    else:
        console.print(table)
        console.print(f"\n[bold]Total tasks for today: {due_count}[/bold]")
        console.print("Use [bold cyan]rvs done <filename>[/bold cyan] after revising.")

@app.command()
def done(filename: str):
    """Mark a revision as complete for a file."""
    db = storage.load_data()
    if filename not in db:
        console.print(f"[red]Error:[/red] '{filename}' is not being tracked.")
        return

    info = db[filename]
    if info['mastered']:
        console.print(f"[green]✨ '{filename}' is already fully mastered![/green]")
        return

    current_stage = info['stage']
    
    if current_stage >= 4:
        info['mastered'] = True
        storage.save_data(db)
        console.print(f"\n[bold green]🎊 CONGRATULATIONS! 🎊[/bold green]")
        console.print(f"[bold]You have completed all 4 revision stages for [cyan]{filename}[/cyan].[/bold]")
        console.print(f"[yellow]This topic is now firmly in your long-term memory. Mastery achieved![/yellow]\n")
    else:
        info['stage'] += 1
        info['next_due'] = scheduler.calculate_next_date(info['stage'])
        storage.save_data(db)
        console.print(f"[bold green]✔ Revision {current_stage} Recorded![/bold green] Next revision due: {info['next_due']}")

if __name__ == "__main__":
    app()