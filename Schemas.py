from marshmallow import Schema, fields, validate

class MotionSensorSchema(Schema):
    motion = fields.Number(required=True)

