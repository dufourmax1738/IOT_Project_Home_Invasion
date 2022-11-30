from marshmallow import Schema, fields, validate

class HomeSchemaPost(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3))
    description = fields.String(required=True, validate=validate.Length(min=5))