from datetime import datetime, timedelta

# This map defines the "Spaced Repetition" intervals.
# Stage 1: +1 day, Stage 2: +3 days, etc.
INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14}

def calculate_next_date(current_stage: int):
    """Calculates the YYYY-MM-DD string for the next revision."""
    days_to_add = INTERVALS.get(current_stage, 0)
    next_date = datetime.now() + timedelta(days=days_to_add)
    return next_date.strftime("%Y-%m-%d")

def determine_status(due_date_str: str, is_mastered: bool):
    """Compares today's date with the due date to return a status label."""
    if is_mastered:
        return "MASTERED"
    
    today = datetime.now().date()
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    
    if today > due_date:
        return "OVERDUE"
    elif today == due_date:
        return "DUE TODAY"
    else:
        return "UPCOMING"