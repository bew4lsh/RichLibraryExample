from rich.console import Console
from rich.markdown import Markdown

def main():
    console = Console()
    console.print("[bold green]Rich Markdown Example[/bold green]\n")

    # Sample Markdown text
    markdown_text = """
# Welcome to Rich Markdown

This is an example of rendering **Markdown** using Rich.

## Features:
- Easy to use
- Supports *italic* and **bold** text
- Renders lists and code blocks

### Code Example:
```python
def greet(name):
    print(f"Hello, {name}!")
```

Visit [Rich documentation](https://rich.readthedocs.io/) for more information.
    """

    # Render the Markdown
    console.print(Markdown(markdown_text))

    console.print("\n[bold cyan]The Markdown above is rendered directly in the terminal![/bold cyan]")

if __name__ == "__main__":
    main()
