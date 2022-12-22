from marshmallow import Schema, fields, validate

class DeviceSchema(Schema):
    name = fields.String(required=True, validate=validate.Regexp("^[a-zA-Z0-9_+-]{3,}$"))

    #these are prone to change depneding on the actual format of the sensorIds
    soundSensorId = fields.Float(required=True)
    motionSensorId = fields.Int(required=True)