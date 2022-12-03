from marshmallow import Schema, fields, validate

class HomeSchemaPost(Schema):
    name = fields.String(required=True, validate=validate.Regexp("^[a-zA-Z0-9_+-]{5,}$"))