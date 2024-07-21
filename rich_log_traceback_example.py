import time
from rich.console import Console
from rich.traceback import install
from rich.logging import RichHandler
import logging
import sys

# Install Rich traceback handler
install(show_locals=True)

# Configure logging with Rich
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_show_locals=True)]
)

log = logging.getLogger("rich")

def simulate_error():
    try:
        1 / 0
    except ZeroDivisionError:
        log.exception("An error occurred!")

def main():
    console = Console()
    
    console.print("[bold green]Rich Log and Traceback Example[/bold green]")
    
    # Logging examples
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    
    # Simulate an error to demonstrate traceback
    console.print("\n[bold red]Simulating an error to demonstrate Rich traceback:[/bold red]")
    simulate_error()
    
    # Demonstrate logging with exception info
    try:
        x = [1, 2, 3]
        print(x[10])
    except IndexError:
        log.exception("An index error occurred!")

if __name__ == "__main__":
    main()
