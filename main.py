from core.database import DatabaseManager
from core.analytics import AnalyticsEngine
from core.reports import ReportGenerator
from core.employee import Employee


class WorkforceApp:

    def __init__(self):
        self.db = DatabaseManager()

    # CRUD
    def add_employee(self, emp):
        self.db.add_employee(emp)

    def get_all(self):
        return self.db.get_all()

    def delete_employee(self, emp_id):
        self.db.delete(emp_id)

    def update_salary(self, emp_id, salary):
        self.db.update(emp_id, salary)

    # analytics
    def get_analytics(self):
        data = self.db.get_all()
        analytics = AnalyticsEngine(data)
        df = analytics.normalize()
        stats = analytics.numpy_stats()

        return df, stats

    # charts
    def generate_reports(self):
        df, _ = self.get_analytics()
        report = ReportGenerator(df)

        return {
            "bar": report.bar(),
            "hist": report.histogram(),
            "scatter": report.scatter(),
            "pie": report.pie()
        }