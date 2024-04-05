from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository

from bookkeeper.view.table_widget import TableWidget
from bookkeeper.view.budget_widget import BudgetWidget
from bookkeeper.view.add_widget import AddWidget


class BudgetMainWindow(QMainWindow):
    def __init__(self, esp_repo: AbstractRepository[Expense], cate_repo: AbstractRepository[Category]):
        super().__init__()
        self.setFixedSize(680, 800)
        self.setWindowTitle("The Bookkeeper App")

        central_widget: QWidget = QWidget(self)
        central_widget.setGeometry(0, 0, self.width(), self.height())
        height = 5
        self._table = TableWidget(parent=central_widget)
        self._table.setGeometry(5, height, self._table.width(), self._table.height())

        height += self._table.height() + 25
        self._budget = BudgetWidget(parent=central_widget)
        self._budget.setGeometry(5, height, self._budget.width(), self._budget.height())

        height += self._budget.height() + 55
        self._add_widget = AddWidget(parent=central_widget)
        self._add_widget.setGeometry(5, height, self._add_widget.width(), self._add_widget.height())

        self.setCentralWidget(central_widget)
        self.show()
