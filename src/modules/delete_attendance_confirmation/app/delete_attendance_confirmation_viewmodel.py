class DeleteAttendanceConfirmationViewmodel:
       activity_code: str
       confirmation_code: str

       def __init__(self, activity_code:str, confirmation_code:str):
              self.activity_code = activity_code
              self.confirmation_code = confirmation_code

       def to_dict(self):
              return {
                     "activity_code": self.activity_code,
                     "confirmation_code": self.confirmation_code,
                     "message": "The confirmation code for the activity was deleted"
              }