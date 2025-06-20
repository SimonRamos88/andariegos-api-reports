from flask import Flask
from .config import Config
from .repository.report_repository import ReportRepository
from .services.report_service import ReportService
from .controllers.report_controller import report_bp
from .controllers.ConsumerQueue import start_consumer
import threading

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize MongoDB connection
    report_repository = ReportRepository(app)
    
    # Initialize services
    report_service = ReportService(report_repository)
    
    # Register blueprints
    app.report_service = report_service  # Attach report_service to the app context
    app.register_blueprint(report_bp, url_prefix='/api/reports')

    threading.Thread(target=start_consumer, args=(app,), daemon=True).start()
    
    return app