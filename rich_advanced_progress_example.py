from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    track,
)
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.console import Console
import time
import random

def spinner_example():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[green]Processing...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.5)
            time.sleep(0.1)

def track_example():
    for value in track(range(100), description="[red]Downloading..."):
        time.sleep(0.05)

def progress_table_example():
    console = Console()
    overall_progress = Progress()
    overall_task = overall_progress.add_task("Overall Progress", total=100)

    progress_table = Table.grid()
    progress_table.add_row(
        Panel.fit(
            overall_progress,
            title="Overall Progress",
            border_style="green",
            padding=(1, 1),
        )
    )

    job_progress = Progress()
    jobs = [
        {"name": "Download", "color": "cyan"},
        {"name": "Process", "color": "magenta"},
        {"name": "Upload", "color": "yellow"},
    ]
    jobs_tasks = {}
    for job in jobs:
        jobs_tasks[job["name"]] = job_progress.add_task(job["name"], total=100)

    progress_table.add_row(
        Panel(job_progress, title="Jobs Progress", border_style="red", padding=(1, 1))
    )

    with Live(progress_table, refresh_per_second=10):
        while not overall_progress.finished:
            for job in jobs:
                if not job_progress.finished:
                    job_progress.update(jobs_tasks[job["name"]], advance=0.5)
            
            completed = sum(task.completed for task in job_progress.tasks)
            overall_progress.update(overall_task, completed=completed / 3)
            time.sleep(0.1)

def main():
    console = Console()
    console.print("[bold green]Rich Advanced Progress Display Examples[/bold green]")

    console.print("\n1. Progress Spinner Example:")
    spinner_example()

    console.print("\n2. Track Progress Example:")
    track_example()

    console.print("\n3. Progress Table Example:")
    progress_table_example()

if __name__ == "__main__":
    main()
