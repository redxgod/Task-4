# Rule-Based Expert System using Backward Chaining

facts = {
    "GoodAttendance",
    "RegularStudy",
    "GoodMarks",
    "ProgrammingSkill"
}

rules = {
    "GoodAcademicPerformance": [
        ["GoodAttendance", "RegularStudy", "GoodMarks"]
    ],

    "EligibleForPlacement": [
        ["GoodAcademicPerformance", "ProgrammingSkill"]
    ],

    "NeedsExtraPractice": [
        ["RegularStudy"]
    ],

    "ReadyForInterview": [
        ["EligibleForPlacement"]
    ]
}


def backward_chaining(goal, visited=None):
    if visited is None:
        visited = set()

    print("Checking:", goal)

    # If goal is already a fact
    if goal in facts:
        print(goal, "is a FACT")
        return True

    # Avoid repeated checking
    if goal in visited:
        return False

    visited.add(goal)

    # Check rules for the goal
    if goal in rules:
        for conditions in rules[goal]:

            print("Rule:", conditions, "->", goal)

            all_true = True

            for condition in conditions:
                if not backward_chaining(condition, visited):
                    all_true = False
                    break

            if all_true:
                return True

    return False


# Selected goal
goal = "EligibleForPlacement"

print("Goal:", goal)
print("----------------------")

result = backward_chaining(goal)

print("----------------------")

if result:
    print("Conclusion:", goal, "is TRUE")
else:
    print("Conclusion:", goal, "is FALSE")
