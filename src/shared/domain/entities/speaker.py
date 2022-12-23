from src.shared.helpers.errors.domain_errors import EntityError


class Speaker:
    name: str
    bio: str
    company: str
    MIN_NAME_LENGTH = 2

    def __init__(self, name, bio, company):
        if not Speaker.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(bio) != str:
            raise EntityError("bio")
        self.bio = bio

        if type(company) != str:
            raise EntityError("company")
        self.company = company


    @staticmethod
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) < Speaker.MIN_NAME_LENGTH:
            return False

        return True

    def __repr__(self):
        return f"Speaker(name={self.name}, bio={self.bio}, company={self.company})"

    def __eq__(self, other):
        return self.name == other.name and self.bio == other.bio and self.company == other.company
