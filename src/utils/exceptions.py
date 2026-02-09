class ResumeAnalyzerError(Exception):
    """Base exception for the application"""
    pass


class ValidationError(ResumeAnalyzerError):
    """Raised when validation fails"""
    pass


class ParseError(ResumeAnalyzerError):
    """Raised when resume parsing fails"""
    pass
