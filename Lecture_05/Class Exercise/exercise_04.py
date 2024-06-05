def computegrade(score):
    try:
        score = float(score)
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
        else:
            return "Bad Score"
    except ValueError:
        return "Bad Score"

score = input("Enter Score: ")
# score = float(score)
ans = computegrade(score)
print(ans)