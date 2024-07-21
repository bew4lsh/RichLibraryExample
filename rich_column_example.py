from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich import box

def create_user_panel(user):
    return Panel(
        f"[bold]{user['name']}[/bold]\n"
        f"[blue]Age:[/blue] {user['age']}\n"
        f"[green]Role:[/green] {user['role']}",
        border_style="cyan",
        box=box.ROUNDED
    )

def main():
    console = Console()

    users = [
        {"name": "Alice", "age": 28, "role": "Developer"},
        {"name": "Bob", "age": 35, "role": "Designer"},
        {"name": "Charlie", "age": 42, "role": "Manager"},
        {"name": "Diana", "age": 31, "role": "Tester"},
        {"name": "Ethan", "age": 39, "role": "Analyst"},
    ]

    user_panels = [create_user_panel(user) for user in users]

    console.print("[bold underline]User Information[/bold underline]")
    console.print(Columns(user_panels))

    console.print("\n[bold green]This is an example of Rich's column output functionality![/bold green]")

if __name__ == "__main__":
    main()
