from marshmallow import Schema, fields, ValidationError

class ReportSchema(Schema):
    id_report = fields.Str(required=True)
    id_tour = fields.Int(required=True)
    id_events = fields.List(fields.Int(), required=True)
    id_reporter = fields.Str(required=True)
    id_reported_users = fields.List(fields.Str(), required=True)
    description = fields.Str()

    class Meta:
        strict = True

def validate_report_data(data):
    schema = ReportSchema()
    errors = schema.validate(data)
    if errors:
        raise ValidationError(errors)

def serialize_report(report):
    schema = ReportSchema()
    return schema.dump(report)