# ...existing code...

from typing import List, Tuple


def gemini_palindrome(s: str) -> bool:
    """
    Gemini-style: ignore non-alphanumeric characters, compare case-insensitively.
    e.g. "A man, a plan, a canal: Panama" -> True
    """
    normalized = "".join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]


def copilot_palindrome(s: str) -> bool:
    """
    Copilot-style (example): ignore whitespace only, compare case-insensitively.
    e.g. "race car" -> True, but "A man, a plan, a canal: Panama" -> False
    """
    stripped = "".join(ch.lower() for ch in s if not ch.isspace())
    return stripped == stripped[::-1]


def compare_functions(
    func_a, func_b, cases: List[str]
) -> List[Tuple[str, bool, bool]]:
    results = []
    for c in cases:
        a = func_a(c)
        b = func_b(c)
        results.append((c, a, b))
    return results


def print_report(results: List[Tuple[str, bool, bool]]):
    matches = 0
    total = len(results)
    print(f"{'input':60} | Gemini | Copilot | status")
    print("-" * 100)
    for s, a, b in results:
        status = "MATCH" if a == b else "DIFFER"
        if status == "MATCH":
            matches += 1
        display = repr(s)
        if len(display) > 58:
            display = display[:55] + "..."
        print(f"{display:60} | {str(a):6} | {str(b):7} | {status}")
    print("-" * 100)
    print(f"Matches: {matches}/{total}  Differences: {total-matches}")


if __name__ == "__main__":
    test_cases = [
        "",  # empty
        "a",
        "Racecar",
        "race car",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "12321",
        "123 321",
        "Was it a car or a cat I saw?",
        "Not a palindrome",
        "!!@@##",  # no alnum
        "あいいあ",  # unicode palindrome
    ]

    results = compare_functions(gemini_palindrome, copilot_palindrome, test_cases)
    print_report(results)