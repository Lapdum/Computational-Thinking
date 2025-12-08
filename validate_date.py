from datetime import datetime

def validate_Date(deadline, date_format=("%d-%m-%Y")):
    try:
        datetime.strptime(deadline, date_format)
        return True,""
    except ValueError as e:
        return False, f"Invalid date format: {e}"