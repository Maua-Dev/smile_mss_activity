from typing import Optional
from src.shared.helpers.errors.domain_errors import EntityError


class Speaker:
    name: Optional[str]
    bio: Optional[str]
    company: Optional[str]
    MIN_NAME_LENGTH = 2

    def __init__(self, name: Optional[str]=None, bio: Optional[str]=None, company: Optional[str]=None):
        if not Speaker.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(bio) != str and bio is not None:
            raise EntityError("bio")
        self.bio = bio

        if type(company) != str and company is not None:
            raise EntityError("company")
        self.company = company


    @staticmethod
    def validate_name(name: str) -> bool:
        if name is not None:
            if type(name) != str:
                return False
            elif len(name) < Speaker.MIN_NAME_LENGTH:
                return False

        return True

    def __repr__(self):
        return f"Speaker(name={self.name}, bio={self.bio}, company={self.company})"

    def __eq__(self, other):
        return self.name == other.name and self.bio == other.bio and self.company == other.company
