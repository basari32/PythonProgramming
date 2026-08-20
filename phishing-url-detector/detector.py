import re

def extract_features(url):
    features = {}

    # Feature 1 - URL Length
    features["url_length"] = len(url)

    # Feature 2 - Has IP address instead of domain
    features["has_ip"] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

    # Feature 3 - Has @ symbol
    features["has_at"] = 1 if "@" in url else 0

    # Feature 4 - Has // in URL
    features["has_double_slash"] = 1 if url.count("//") > 1 else 0

    # Feature 5 - HTTPS or not
    features["has_https"] = 1 if url.startswith("https") else 0

    # Feature 6 - Number of subdomains
    features["subdomains"] = len(url.split(".")) - 2

    # Feature 7 - Suspicious words
    suspicious_words = ["login", "verify", "secure", "banking", "update", "free", "lucky"]
    features["has_suspicious_words"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    return features


def detect_phishing(url):
    features = extract_features(url)
    score = 0

    if features["url_length"] > 75:
        score += 2
    if features["has_ip"]:
        score += 3
    if features["has_at"]:
        score += 2
    if features["has_double_slash"]:
        score += 2
    if not features["has_https"]:
        score += 2
    if features["subdomains"] > 3:
        score += 2
    if features["has_suspicious_words"]:
        score += 2

    if score >= 5:
        return "Phishing", score, features
    else:
        return "Legitimate", score, features