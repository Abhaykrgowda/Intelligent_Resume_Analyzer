class Job:
    def __init__(self, title, required_skills, min_experience, education):
        self.title = title
        self.required_skills = required_skills
        self.min_experience = min_experience
        self.education = education

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create Job object from dictionary (e.g. loaded from JSON)
        """
        return cls(
            title=data.get("title"),
            required_skills=data.get("required_skills", []),
            min_experience=data.get("min_experience", 0),
            education=data.get("education")
        )
