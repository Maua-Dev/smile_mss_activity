from src.modules.delete_attendance_confirmation.app.delete_attendance_confirmation_viewmodel import DeleteAttendanceConfirmationViewmodel


class Test_DeleteAttendanceConfirmationViewmodel:
       def test_delete_attendance_confirmation_viewmodel(self):
              viewmodel = DeleteAttendanceConfirmationViewmodel(activity_code="555666", confirmation_code=None)

              assert viewmodel.activity_code == "555666"
              assert viewmodel.to_dict() == {
                     "activity_code": "555666",
                     "confirmation_code": None,
                     "message": "The confirmation code for the activity was deleted"
              }