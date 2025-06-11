from ..repository.report_repository import ReportRepository
from ..schemas.report_schema import validate_report_data, serialize_report

class ReportService:
    def __init__(self, repository):
        self.repository = repository
    
    def create_report(self, report_data):
        validate_report_data(report_data)
        return self.repository.create_report(report_data)
    
    def get_report(self, report_id):
        report = self.repository.get_report(report_id)
        if report:
            return serialize_report(report)
        return None
    
    def get_all_reports(self):
        reports = self.repository.get_all_reports()
        return [serialize_report(report) for report in reports]
    
    def update_report(self, report_id, report_data):
        validate_report_data(report_data)
        return self.repository.update_report(report_id, report_data)
    
    def delete_report(self, report_id):
        return self.repository.delete_report(report_id)