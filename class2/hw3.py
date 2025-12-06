score = int(input("請輸入成績:"))
if score >= 90 and score <= 100:
    print("你的成績等第是A!")
elif score >= 80 and score < 90:
    print("你的成績等第是B!")
elif score >= 70 and score < 80:
    print("你的成績等第是C!")
elif score >= 60 and score < 70:
    print("你的成績等第是D!")
elif score >= 0 and score < 60:
    print("你的成績等第是F!")
