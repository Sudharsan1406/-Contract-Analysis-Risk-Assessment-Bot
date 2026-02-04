if "unilateral" and "terminate":
    risk = HIGH
    reason = "Only one party can terminate"


if "without notice" in text:
    risk = "High"
elif unilateral_termination:
    risk = "High"
elif notice_days > 60:
    risk = "Medium"
else:
    risk = "Low"