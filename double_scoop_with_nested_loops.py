#task1
import random
moods = ["happy","sad","energetic","calm","tired"]
weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(len(weekday)):
    for time in ["Morning", "Afternoon", "Night"]:
        mood = random.choice(moods)
        print(f"On {weekday[i]} {time} I was {mood}.")
else:
    print("The week has ended.")
