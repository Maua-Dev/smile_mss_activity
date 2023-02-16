class GenerateAttendanceConfirmationViewmodel:
    confirmation_code: str
    activity_code: str

    def __init__(self, confirmation_code: str, activity_code: str):
        self.confirmation_code = confirmation_code
        self.activity_code = activity_code

    def to_dict(self):
        return {
            "confirmation_code": self.confirmation_code,
            "activity_code": self.activity_code,
            "message": "The confirmation code for the activity was generated successfully"
        }
