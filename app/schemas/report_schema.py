from marshmallow import Schema, fields, ValidationError, validate

class ReportSchema(Schema):
    _id = fields.Str()
    id_events = fields.List(fields.Int(), required=True)
    id_reporter = fields.Str(required=True)
    state = fields.Str(required=True, validate=validate.OneOf(['accepted', 'denied', 'pending']))
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