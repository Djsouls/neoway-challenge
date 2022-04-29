from validate_docbr import BaseDoc

def validate(validator: BaseDoc, content: str) -> bool:
    return validator.validate(content)