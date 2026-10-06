from laya import Router
from cases import cases

router = Router()


questions = {
    "category": {
        "type": "choice",
        "instructions": "Qual categoria melhor descreve o problema?",
        "criteria": [
            "security",
            "backend",
            "frontend",
            "infrastructure",
        ],
    }
}

total = 0
correct_count = 0


category_stats = {
    "security": {"total": 0, "correct": 0},
    "backend": {"total": 0, "correct": 0},
    "frontend": {"total": 0, "correct": 0},
    "infrastructure": {"total": 0, "correct": 0},
}

confusion_matrix = {
    "security": {
        "security": 0,
        "backend": 0,
        "frontend": 0,
        "infrastructure": 0,
    },
    "backend": {
        "security": 0,
        "backend": 0,
        "frontend": 0,
        "infrastructure": 0,
    },
    "frontend": {
        "security": 0,
        "backend": 0,
        "frontend": 0,
        "infrastructure": 0,
    },
    "infrastructure": {
        "security": 0,
        "backend": 0,
        "frontend": 0,
        "infrastructure": 0,
    },
}


for case in cases:
    result = router.predict(case["state"], questions)
    answer = result["answers"]["category"]

    correct = answer["choice"] == case["expected"]
    category = case["expected"]
    predicted = answer["choice"]

    confusion_matrix[category][predicted] += 1

    category_stats[category]["total"] += 1

    if correct:
        category_stats[category]["correct"] += 1

    total += 1

    if correct:
        correct_count += 1

    print("=" * 70)
    print(case["name"])
    print("Expected:", case["expected"])
    print("Predicted:", answer["choice"])
    print("Correct:", correct)
    print("Answer confidence:", answer["answer_confidence"])
    print("Confidence:", answer["confidence"])


print()
print("=" * 70)
print("BENCHMARK")
print("=" * 70)

accuracy = correct_count / total

print("Total:", total)
print("Correct:", correct_count)
print("Accuracy:", f"{accuracy:.2%}")


print()
print("=" * 70)
print("ACCURACY BY CATEGORY")
print("=" * 70)

print()
print("=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)

categories = [
    "security",
    "backend",
    "frontend",
    "infrastructure",
]

print(
    f"{'Expected':<18}"
    f"{'security':>12}"
    f"{'backend':>12}"
    f"{'frontend':>12}"
    f"{'infrastructure':>16}"
)

for expected in categories:
    print(
        f"{expected:<18}"
        f"{confusion_matrix[expected]['security']:>12}"
        f"{confusion_matrix[expected]['backend']:>12}"
        f"{confusion_matrix[expected]['frontend']:>12}"
        f"{confusion_matrix[expected]['infrastructure']:>16}"
    )

for category, stats in category_stats.items():
    accuracy = stats["correct"] / stats["total"]

    print(
        f"{category}: "
        f"{stats['correct']}/{stats['total']} "
        f"({accuracy:.2%})"
    )
