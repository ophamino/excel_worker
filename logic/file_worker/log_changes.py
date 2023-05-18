import os

from openpyxl import load_workbook


class LogChanges:
    """Класс журнала изменений"""

    def __init__(self, static_file: str, changes: str, log_name: str) -> None:
        self.static_file = static_file
        self.changes = changes
        self.log_name = log_name

    def checl_cell() -> None:
        pass
