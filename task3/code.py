import re

def validate_seating(matrix):
    seen_rolls = set()
    errors = []
    empty_count = 0
    reserved_count = 0
    pattern = re.compile(r"^STU\d{3}$")
    
    for r_idx, row in enumerate(matrix):
        for c_idx, seat in enumerate(row):
            if seat is None or seat == "EMPTY":
                empty_count += 1
            elif seat == "RESERVED":
                reserved_count += 1
            elif isinstance(seat, str):
                if not pattern.match(seat):
                    errors.append(f"Invalid format at ({r_idx}, {c_idx}): {seat}")
                elif seat in seen_rolls:
                    errors.append(f"Duplicate roll number at ({r_idx}, {c_idx}): {seat}")
                else:
                    seen_rolls.add(seat)
            else:
                errors.append(f"Invalid data type at ({r_idx}, {c_idx}): {seat}")
                
    return {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "empty_seats": empty_count,
        "reserved_seats": reserved_count,
        "unique_students": len(seen_rolls)
    }
