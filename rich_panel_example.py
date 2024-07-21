from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Create a console object
console = Console()

# Create a simple panel
simple_panel = Panel("This is a simple panel")
console.print(simple_panel)

# Create a panel with a title
titled_panel = Panel("This panel has a title", title="Panel Title")
console.print(titled_panel)

# Create a panel with custom border style
styled_panel = Panel("This panel has a custom border style", border_style="red")
console.print(styled_panel)

# Create a panel with rich content
rich_content = Text.assemble(
    ("This is ", "bold"),
    ("rich ", "italic red"),
    ("content", "underline green"),
)
rich_panel = Panel(rich_content, expand=False)
console.print(rich_panel)

# Create a nested panel
inner_panel = Panel("I'm an inner panel")
outer_panel = Panel(inner_panel, title="Outer Panel")
console.print(outer_panel)
