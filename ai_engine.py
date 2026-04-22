def predict_risk(f):
    score = 0
    issues = []
    suggestions = []

    if f["lines"] > 50:
        score += 20
        issues.append("Large function")
        suggestions.append("Break into smaller methods")

    if f["nesting"] > 10:
        score += 20
        issues.append("Deep nesting")
        suggestions.append("Reduce nested blocks")

    if f["loops"] > 3:
        score += 15
        issues.append("Too many loops")
        suggestions.append("Optimize loops")

    if f["ifs"] > 5:
        score += 15
        issues.append("Too many conditions")
        suggestions.append("Simplify logic")

    if f["null_checks"] == 0:
        score += 20
        issues.append("No null checks")
        suggestions.append("Add null validations")

    # Risk classification
    if score < 30:
        risk = "LOW"
    elif score < 60:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "score": score,
        "risk": risk,
        "issues": issues,
        "suggestions": suggestions
    }
