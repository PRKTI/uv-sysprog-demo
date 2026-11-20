import psutil
import requests
from rich.console import Console
from rich.table import Table

console = Console()


def main():
    console.print("[bold cyan]Системный мониторинг и проверка сети[/bold cyan]\n")
    cpu_usage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    try:
        response = requests.get("https://httpbin.org/get", timeout=5)
        net_status = f"[green]Доступно (HTTP {response.status_code})[/green]"
    except requests.RequestException:
        net_status = "[red]Ошибка соединения[/red]"
    table = Table(title="Статус рабочей станции")
    table.add_column("Параметр", style="bold yellow")
    table.add_column("Значение", style="white")

    table.add_row("Загрузка CPU", f"{cpu_usage}%")
    table.add_row("Использование ОЗУ", f"{memory.percent}% ({round(memory.used / (1024**3), 2)} ГБ)")
    table.add_row("Состояние сети", net_status)

    console.print(table)


if __name__ == "__main__":
    main()