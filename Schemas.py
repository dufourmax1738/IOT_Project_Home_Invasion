from marshmallow import Schema, fields, validate

class SoundSensorSchema(Schema):
    sound = fields.Float(required=True)