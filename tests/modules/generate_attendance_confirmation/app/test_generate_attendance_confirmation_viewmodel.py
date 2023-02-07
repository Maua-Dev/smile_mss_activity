from src.modules.generate_attendance_confirmation.app.generate_attendance_confirmation_viewmodel import \
    GenerateAttendanceConfirmationViewmodel


class Test_GenerateAttendanceConfirmationViewmodel:
    def test_generate_attendance_confirmation(self):
        viewmodel = GenerateAttendanceConfirmationViewmodel(confirmation_code="123456", activity_code="ELETRO123")

        assert viewmodel.confirmation_code == "123456"
        assert viewmodel.activity_code == "ELETRO123"
        assert viewmodel.to_dict() == {
            "confirmation_code": "123456",
            "activity_code": "ELETRO123",
            "message": "The confirmation code for the activity was generated successfully"
        }
