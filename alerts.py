def check_alert(current_count, threshold=15):
    if current_count > threshold:
        return True, "Crowd limit exceeded"
    return False, ""
