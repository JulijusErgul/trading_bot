from rich.console import Console
from rich.table import Table

console = Console()

def display_signal(df, signal):
    table = Table(title="Trading Dashboard")

    table.add_column("Symbol", justify="left")
    table.add_column("Latest Close", justify="right")
    table.add_column("SMA Fast", justify="right")
    table.add_column("SMA Slow", justify="right")
    table.add_column("Signal", justify="center")

    latest_close = f"{df['c'].iloc[-1]:.2f}"
    sma_fast = f"{df['sma_fast'].iloc[-1]:.2f}"
    sma_slow = f"{df['sma_slow'].iloc[-1]:.2f}"

    table.add_row(df['S'].iloc[-1] if 'S' in df else 'N/A', latest_close, sma_fast, sma_slow, signal)

    console.print(table)
