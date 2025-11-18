def analyze_workouts(workouts):
    #if user has no workouts
    if not workouts:
        return "Bro... you havent lifted anything yet 😂 Log at leatst one workout."
    #Step 1: Extract all weights from the workouts
    weights = [w["weight"] for w in workouts]

    #Step 2: Find max weight
    max_weight = max(weights)
    #Step 3: Find average weight
    avg_weight = sum(weights) / len(weights)

    #Step 4: Start AI logic (simple)
    if max_weight < 40:
        return "Bro... those weights are lighter than your phone 😂 Try going heavier."
    
    if avg_weight < 60:
        return "Decent lifting bro. Increase weights by 5-10% weekly for real gains. "
    return "BROOO you're lifting serious plates 🔥🔥 keep pushing!"

#---------Analyze Nutrition ------------

def analyze_nutrition(nutrition_log):
    # If no meals logged
    if not nutrition_log:
        return "Bro... you didnt log any meals. Even the legends eat."
    
    #Get totals
    total_protein = sum(item["protein"] for item in nutrition_log)
    total_carbs = sum(item["carbs"] for item in nutrition_log)
    total_fats = sum(item["fats"] for item in nutrition_log)

    #Start building advice

    advice_parts = []

    if total_protein < 100:
        advice_parts.append("Protein low 💀 - aim for ~1.6/kg bodyweight. Add a shake or chicken.")
    if total_carbs < 150:
        advice_parts.append("Carbs low - muscles need glycogen for heavy sets. Add a shake or oats.")
    if total_fats < 40:
        advice_parts.append("Fats low - healthy fats help hormones. Add nuts or olive oil.")

    if not advice_parts:
        return "Nutrition ON POINT 🦍🔥. Keep the macros steady for gains."
    
    #Join all advice pieces into 1 string
    return "\n".join(advice_parts)


#------------Analyze sleep----------

def analyze_sleep(sleep_log):
    #sleep_log is expected to be a list of numbers(hours)

    if not sleep_log:
        return "Sleep log empty. Bro... you can't out train bad sleep."
    avg_sleep = sum(sleep_log) / len(sleep_log)

    if avg_sleep < 6:
        return "BROOO 😭 - avg <6h. Cortisol up, recovery down. Aim 7-9 hours."
    if avg_sleep < 7.5:
        return "Decent sleep bro. Target 7.5-8.5 for better recovery."
    return "Sleep is SOLID 🔥. Recovery and hormone balance look good."

#--------------full_coach_feedback()----------------

import openai  # Make sure your OPENAI_API_KEY is set in your environment

def get_chatgpt_feedback(workouts, nutrition_log, sleep_log):
    """Helper function to get ChatGPT-generated advice"""
    
    # Prepare summaries
    workouts_summary = "\n".join([f"{w['name']}: {w['reps']} reps x {w['weight']}kg" for w in workouts]) if workouts else "No workouts logged."
    nutrition_summary = "\n".join([f"{n['food']} -> P:{n['protein']}g C:{n['carbs']}g F:{n['fats']}g" for n in nutrition_log]) if nutrition_log else "No meals logged."
    sleep_hours_only = [s['hours'] for s in sleep_log if isinstance(s, dict)]
    sleep_summary = f"Average sleep hours: {sum(sleep_hours_only)/len(sleep_hours_only):.2f}" if sleep_hours_only else "No sleep data."

    prompt = f"""
    You are a smart, motivating fitness coach. Analyze the following user logs and give friendly advice:

    Workouts:
    {workouts_summary}

    Nutrition:
    {nutrition_summary}

    Sleep:
    {sleep_summary}

    Give short actionable tips and encouragement.
    """

    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a friendly, motivating fitness coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()


def full_coach_feedback(workouts, nutrition_log, sleep_log):
    """Combines static feedback with ChatGPT advice"""
    
    # ANSI color codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    # Static feedback
    from ai_coach import analyze_workouts, analyze_nutrition, analyze_sleep  # make sure these are in the same file

    parts = []
    parts.append(f"{YELLOW}=== 🤖 AI Coach Report ==={RESET}")
    parts.append(f"\n🏋️ {CYAN}Workout Feedback:{RESET}")
    parts.append(f"{GREEN}{analyze_workouts(workouts)}{RESET}")
    parts.append(f"\n🥗 {CYAN}Nutrition Feedback:{RESET}")
    parts.append(f"{GREEN}{analyze_nutrition(nutrition_log)}{RESET}")
    parts.append(f"\n😴 {CYAN}Sleep Feedback:{RESET}")
    parts.append(f"{GREEN}{analyze_sleep(sleep_log)}{RESET}")
    parts.append(f"\n{YELLOW}Keep grinding - consistency > intensity, bro. 💪{RESET}")

    static_feedback = "\n\n".join(parts)

    # Add ChatGPT advice
    try:
        chat_feedback = get_chatgpt_feedback(workouts, nutrition_log, sleep_log)
        return static_feedback + "\n\n" + f"{CYAN}💡 ChatGPT Advice:{RESET}\n" + chat_feedback
    except Exception as e:
        return static_feedback + f"\n\n{CYAN}⚠️ ChatGPT advice unavailable:{RESET} {e}"
