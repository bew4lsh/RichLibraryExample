import time
from datetime import datetime
import psutil
from rich.live import Live
from rich.table import Table
from rich import box

def get_system_info():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    ram_percent = memory.percent
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time, cpu_percent, ram_percent

def generate_table(data):
    table = Table(title="System Information", box=box.ROUNDED)
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    table.add_row("Current Time", data[0])
    table.add_row("CPU Utilization", f"{data[1]}%")
    table.add_row("RAM Utilization", f"{data[2]}%")
    
    return table

with Live(refresh_per_second=1) as live:
    while True:
        live.update(generate_table(get_system_info()))
        time.sleep(1)
