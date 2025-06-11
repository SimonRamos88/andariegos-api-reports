from pymongo import MongoClient

class ReportRepository:
    def __init__(self, app):
        self.client = MongoClient(app.config['MONGO_URI'])
        self.db = self.client['andariegos']
        self.collection = self.db['Reports']
    
    def create_report(self, report_data):
        return self.collection.insert_one(report_data)
    
    def get_report(self, report_id):
        return self.collection.find_one({'id_report': report_id})
    
    def get_all_reports(self):
        return list(self.collection.find())
    
    def update_report(self, report_id, report_data):
        return self.collection.update_one({'id_report': report_id}, {'$set': report_data})
    
    def delete_report(self, report_id):
        return self.collection.delete_one({'id_report': report_id})