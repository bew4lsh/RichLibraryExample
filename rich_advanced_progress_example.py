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


def advanced_progress_example():
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    ) as progress:
        task1 = progress.add_task("[red]Downloading...", total=1000)
        task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[blue]Uploading...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=9)
            progress.update(task2, advance=5)
            progress.update(task3, advance=3)
            time.sleep(0.1)


def spinner_example():
    # Create a progress bar with a spinner and text columns
    with Progress(
        SpinnerColumn(),  # Spinner column to show a spinning animation
        TextColumn(
            "[progress.description]{task.description}"
        ),  # Text column to display task description
        transient=True,  # Set transient to True to clear the progress bar after completion
    ) as progress:
        # Add a task to the progress bar with a description and total steps
        task = progress.add_task("[green]Processing...", total=100)
        # Update the progress bar until it's finished
        while not progress.finished:
            # Update the task progress by 0.5 units
            progress.update(task, advance=0.5)
            # Pause for a short time to simulate processing
            time.sleep(0.1)


def track_example():
    # Loop through a range of 100 values while displaying a custom description
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

    console.print("\n4. Advanced Progress Bar Example:")
    advanced_progress_example()


if __name__ == "__main__":
    main()
