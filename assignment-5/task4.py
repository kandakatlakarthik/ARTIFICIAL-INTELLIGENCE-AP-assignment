"""
Simple interactive scoring system for job applicants.

Features collected:
 - years_experience (capped)
 - education_level (mapped)
 - skills_match (percentage)
 - certifications_count (capped)
 - interview_score (0-100)
 - cultural_fit (1-5)

Each feature is normalized to 0-100, multiplied by a weight, and combined into
a final score (0-100). The script classifies applicants into tiers.
"""

def prompt_int(prompt, min_value=None, max_value=None):
    """Prompt for an integer with optional min/max validation."""
    while True:
        try:
            v = int(input(prompt).strip())
            if (min_value is not None and v < min_value) or (max_value is not None and v > max_value):
                print(f"Please enter an integer between {min_value} and {max_value}.")
                continue
            return v
        except ValueError:
            print("Invalid integer. Try again.")

def prompt_float(prompt, min_value=None, max_value=None):
    """Prompt for a float with optional min/max validation."""
    while True:
        try:
            v = float(input(prompt).strip())
            if (min_value is not None and v < min_value) or (max_value is not None and v > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return v
        except ValueError:
            print("Invalid number. Try again.")

def normalize_years(exp, cap=20):
    """Normalize years of experience to 0-100 (cap controls saturation)."""
    return min(exp, cap) / cap * 100

def map_education(level):
    """Map textual education level to a 0-100 score."""
    mapping = {
        "highschool": 40,
        "associate": 60,
        "bachelor": 80,
        "master": 90,
        "phd": 95
    }
    return mapping.get(level.lower(), 0)

def normalize_certifications(count, cap=10):
    """Normalize certifications count to 0-100 (cap controls saturation)."""
    return min(count, cap) / cap * 100

def normalize_cultural_fit(score, min_scale=1, max_scale=5):
    """Normalize cultural fit scale (e.g., 1-5) to 0-100."""
    return (score - min_scale) / (max_scale - min_scale) * 100

def compute_final_score(features, weights):
    """Compute weighted normalized final score (0-100)."""
    weighted_sum = 0.0
    weight_total = 0.0
    for key, value in features.items():
        w = weights.get(key, 0)
        weighted_sum += w * value
        weight_total += w
    if weight_total == 0:
        return 0.0
    return weighted_sum / weight_total

def classify_score(score):
    """Simple tiering of final score."""
    if score >= 85:
        return "Hire"
    if score >= 70:
        return "Strong Consider"
    if score >= 50:
        return "Consider"
    return "Reject"

def main():
    print("Applicant scoring system - provide applicant features.\n")

    # Collect raw inputs
    years = prompt_int("Years of experience (integer): ", min_value=0)
    print("Education levels: highschool, associate, bachelor, master, phd")
    edu = input("Education level: ").strip()
    skills_pct = prompt_float("Skills match percentage (0-100): ", 0, 100)
    certs = prompt_int("Number of relevant certifications (integer): ", min_value=0)
    interview = prompt_float("Interview score (0-100): ", 0, 100)
    cultural = prompt_int("Cultural fit rating (1-5): ", min_value=1, max_value=5)

    # Default weights (adjustable if desired)
    weights = {
        "experience": 0.20,
        "education": 0.15,
        "skills": 0.30,
        "certifications": 0.05,
        "interview": 0.25,
        "cultural": 0.05
    }

    # Normalize features to 0-100
    features = {
        "experience": normalize_years(years),
        "education": map_education(edu),
        "skills": skills_pct,
        "certifications": normalize_certifications(certs),
        "interview": interview,
        "cultural": normalize_cultural_fit(cultural)
    }

    final = compute_final_score(features, weights)
    tier = classify_score(final)

    # Output summary
    print("\nFeature scores (0-100):")
    for k, v in features.items():
        print(f" - {k:13}: {v:.1f}")
    print(f"\nFinal weighted score: {final:.2f}/100")
    print(f"Recommendation: {tier}")

if __name__ == "__main__":
    main()