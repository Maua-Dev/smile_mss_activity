from src.shared.helpers.errors.base_error import BaseError

class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(message)
        
class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class UserAlreadyEnrolled(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class ClosedActivity(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class ConflictingInformation(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class UserAlreadyCompleted(BaseError):
    def  __init__(self, message: str):
        super().__init__(message)

class ActivityEnded(BaseError):
    def  __init__(self, message: str):
        super().__init__(message)

class UserNotAdmin(BaseError):
    def  __init__(self, message: str):
        super().__init__(message)
        
class UnecessaryUpdate(BaseError):
    def  __init__(self, message: str):
        super().__init__(message)

class ImpossibleEnrollment(BaseError):
    def  __init__(self, message: str):
        super().__init__(message)
