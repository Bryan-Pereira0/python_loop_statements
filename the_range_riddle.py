import random
moods = ["happy","sad","energetic","calm"]
weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(len(weekday)):
        print(f"On {weekday[i]} you felt {random.choice (moods)}.")
else:
    print("The week has ended.")
    