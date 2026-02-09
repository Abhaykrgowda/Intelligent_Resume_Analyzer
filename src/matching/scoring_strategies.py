class ScoringStrategy:
    def calculate(self, candidate, job):
        raise NotImplementedError


class BasicScoring(ScoringStrategy):
    def calculate(self, candidate, job):
        score = 0

        matched = set(candidate.skills) & set(job.required_skills)
        score += len(matched) * 10

        if candidate.experience >= job.min_experience:
            score += 30

        if candidate.education == job.education:
            score += 20

        return min(score, 100)


class WeightedScoring(ScoringStrategy):
    def calculate(self, candidate, job):
        score = 0

        score += len(set(candidate.skills) & set(job.required_skills)) * 15
        score += min(candidate.experience, job.min_experience) * 5

        return min(score, 100)
