from analyzer import analyze_code

def main():
    with open("sample_code.txt", "r") as f:
        code = f.read()

    result = analyze_code(code)

    print("\n=== AI BUG PREDICTION ===")
    print("Risk Level:", result["risk"])
    print("Bug Probability:", result["score"], "%")
    print("Issues Found:", result["issues"])
    print("Suggestions:", result["suggestions"])

if __name__ == "__main__":
    main()
