from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box

def main():
    console = Console()
    console.print("[bold green]Rich Layout Example[/bold green]\n")

    # Create the layout
    layout = Layout()

    # Split the layout into three sections
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )

    # Split the body into two columns
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    # Add content to each section
    layout["header"].update(Panel("Header", style="on blue"))
    layout["left"].update(Panel("Left Column", box=box.ROUNDED))
    layout["right"].update(Panel("Right Column", box=box.ROUNDED))
    layout["footer"].update(Panel("Footer", style="on red"))

    # Print the layout
    console.print(layout)

if __name__ == "__main__":
    main()
