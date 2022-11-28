from marshmallow import Schema, fields, validate

class SoundSensorSchema(Schema):
    motion = fields.Number(required=True)

