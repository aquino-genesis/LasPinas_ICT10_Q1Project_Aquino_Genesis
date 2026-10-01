import re
import string

# Text Tag Stripper
def cleanText(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'https?://\s+|www\.\s+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split())
    return text

# Error String Generator
def generateError(msg, title="Error", extraClasses=""):
    return f"<span class='fw-bold text-danger {extraClasses}'>{title}:</span><br>{str(msg)}"

# Success String Generator
def generateSuccess(msg, title="Success", extraClasses=""):
    return f"<span class='fw-bold text-success {extraClasses}'>{title}:</span><br>{str(msg)}"