from marshmallow import Schema, fields, validate

class SoundSensorSchema(Schema):
    sound = fields.Float(required=True)

class MotionSensorSchema(Schema):
    motion = fields.Number(required=True)