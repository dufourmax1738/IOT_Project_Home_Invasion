from marshmallow import Schema, fields, validate

class SoundSensorSchema(Schema):
    sound = fields.Number(required=True)