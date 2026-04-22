def extract_features(code):
    lines = code.split("\n")

    num_lines = len(lines)
    num_ifs = code.count("if")
    num_loops = code.count("for") + code.count("while")
    nesting = code.count("{")  # simple approximation
    null_checks = code.count("null")

    return {
        "lines": num_lines,
        "ifs": num_ifs,
        "loops": num_loops,
        "nesting": nesting,
        "null_checks": null_checks
    }
