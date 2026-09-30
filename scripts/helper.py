# Error String Generator
def generateError(msg, title="Error", extraClasses=""):
    return f"<span class='fw-bold text-danger {extraClasses}'>{title}:</span><br>{str(msg)}"

# Success String Generator
def generateSuccess(msg, title="Success", extraClasses=""):
    return f"<span class='fw-bold text-success {extraClasses}'>{title}:</span><br>{str(msg)}"