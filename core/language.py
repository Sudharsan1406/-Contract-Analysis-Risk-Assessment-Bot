from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


def detect_language(text):
    """
    Detect language of the contract text.
    Returns 'en' for English or 'hi' for Hindi.
    Defaults to 'en' if detection fails.
    """
    try:
        lang = detect(text)
        if lang == "hi":
            return "hi"
        return "en"
    except LangDetectException:
        return "en"


def normalize_to_english(text):
    if text is None:
        return ""

    lang = detect_language(text)

    if lang == "en":
        return text

    # TEMP: no translation yet
    return text

