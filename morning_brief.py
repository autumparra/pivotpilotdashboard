from fetch_emails import fetch_recent_emails
import random

def generate_morning_brief():
    emails = fetch_recent_emails(limit=5)
    
    highlights = []
    for mail in emails[:3]:
        highlights.append(f"📧 {mail['subject']}")
    
    action_items = [
        "✅ Apply to 2 cybersecurity roles",
        "📅 Finish math homework",
        "💧 Water the plants",
        "🐱 Scoop the poopy zen garden",
        "🍽️ Do the dishes"
    ]
    
    motivations = [
        "Small steps every day lead to big career changes. You're doing great, Autum.",
        "Progress over perfection. Keep going.",
        "One focused hour today beats 3 distracted ones."
    ]
    
    brief = f"""🐈‍⬛ **Pivot Pilot Morning Brief**

**Highlights**
{chr(10).join(highlights) if highlights else "• No new recruiter emails today"}

**Top Action Items**
{chr(10).join(action_items)}

**Chore Reminders**
• Water the plants 🌱
• Scoop the poopy zen garden 🐾
• Do the dishes 🍽️

**Motivation**
{random.choice(motivations)}

Have a strong day 💪
"""
    return brief

if __name__ == "__main__":
    print(generate_morning_brief())