import datetime
import random

tasks = [
    "Build one small Python script",
    "Add a new feature to your AI assistant",
    "Learn one new Python concept and test it",
    "Automate something annoying on your PC",
    "Push something to GitHub",
]

quotes = [
    "No zero days. One output minimum.",
    "Move first, then build.",
    "90-day experiments. Stop overthinking.",
    "Builder: Body + Skill + Discipline.",
    "Does this improve your body, skill, or future? If no, skip.",
]

day = datetime.datetime.now().strftime("%A, %d %B %Y")
task = random.choice(tasks)
quote = random.choice(quotes)

today = datetime.date.today().isoformat()
yesterday = datetime.date.today() - datetime.timedelta(days=1)

with open("streak.txt","r") as f:
    last_date=f.read()
if last_date == yesterday.isoformat():
    print("Streak ALIVE.")
else:
    print("Zero Day")

with open("streak.txt","w") as f:
    f.write(today)


print("=" * 45)
print(f"  📅 {day}")
print("=" * 45)
print()
print("🔵 BODY:  Cycle or walk today. No excuse.")
print("🟢 SKILL: Python — build something small.")
print()
print(f"⚡ TODAY'S TASK:\n   {task}")
print()
print(f"💬 REMINDER:\n   {quote}")
print()
print("=" * 45)
print("  No zero days, Arshad.")
print("=" * 45)
input("\nPress Enter to close...")