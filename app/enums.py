from enum import StrEnum


class Status(StrEnum):
    """
    Enum representing all possible workflow statuses.
    """

    PENDING = "pending"
    PROCESSING = "processing"
    OCR_PARSED = "ocr_parsed"
    LLM_ANALYZED = "llm_analyzed"
    STORED_IN_STORAGE = "stored_in_storage"
    ERROR = "error"
    SUCCESS = "success"


class Category(StrEnum):
    """
    Enum representing all possible document categories.
    """

    PREDEFINED = "predefined"
    CUSTOM = "custom"
