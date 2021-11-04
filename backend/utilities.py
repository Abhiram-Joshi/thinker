def response_writer(status: str, data: dict, code: int, message: str) -> dict:
    return {
        "status": status,
        "data": data,
        "code": code,
        "message": message,
    }

def get_model_fields(model):
    return [field.name for field in model._meta.fields if field.name not in ["password", "last_login", "is_superuser"]]