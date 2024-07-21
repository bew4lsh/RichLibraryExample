from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.console import Console
import time
import random

def simulate_task(task_id, progress):
    total = 100
    for i in range(total):
        time.sleep(0.1)  # Simulate some work
        progress.update(task_id, advance=1, description=f"Task {task_id} processing...")
        if random.random() < 0.05:
            progress.console.print(f"[yellow]Info: Something happened in task {task_id}[/yellow]")

def main():
    console = Console()
    console.print("[bold green]Rich Progress Bar Example[/bold green]")

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        task1 = progress.add_task("[red]Processing...", total=100)
        task2 = progress.add_task("[green]Analyzing...", total=100)
        task3 = progress.add_task("[blue]Finalizing...", total=100)

        simulate_task(task1, progress)
        simulate_task(task2, progress)
        simulate_task(task3, progress)

    console.print("[bold]All tasks completed![/bold]")

if __name__ == "__main__":
    main()
