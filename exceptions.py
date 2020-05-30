class BaseError(Exception):
    def __init__(self, code=400, message="", status="", field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field
        self.success = False

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "status": self.status,
            "field": self.field,
            "success": self.success
        }


class AppValidationError(BaseError):
    def __init__(self, field, message="Invalid field"):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = "INVALID_FIELD"
        self.field = field