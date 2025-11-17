#Workout Logging Module
import json
#File to store workout data
DATA_FILE = 'workout_data.json'
#Load existing data if available 
try:
    with open(DATA_FILE, "r") as f:
        workouts = json.load(f)
except FileNotFoundError:
    workouts = []

#Function to add a new exercise
def add_exercise():
    name = input("Exercise name:")
    reps = int(input("Reps: "))
    weight = float(input("weight (kg): "))
    workouts.append({"name": name, "reps": reps, "weight": weight})
    print(f"{name} added successfully!\n")

#Function to show summary
def show_summary():
    if not workouts:
        print("No workouts logged yet. \n")
        return
    print("\n--- Workout Summary ---")
    total_reps = 0
    max_weight = 0
    total_weight = 0
    for ex in workouts:
        print(f"{ex['name']}: {ex['reps']} reps x {ex['weight']} kg")
        total_reps += ex['reps']
        total_weight += ex['weight']
        if ex['weight'] > max_weight:
            max_weight = ex['weight']

    average_weight = total_weight / len(workouts)
    print(f"\nTotal reps: {total_reps}")
    print(f"Max weight lifted: {max_weight} kg")
    print(f"Average weight lifted: {average_weight:.2f} kg\n")

#Save data
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(workouts, f)
    print("Workout data saved! \n")


#-----------------Nutrition Tracking Module ---------------

#File to store nutrition data

NUTRITION_FILE = "nutrition_data.json"

#Load existing nutrition data

try:
    with open(NUTRITION_FILE, "r") as f:
        nutrition_log = json.load(f)
except FileNotFoundError:
    nutrition_log = []


#Add food entry

def add_meal():
    print("\n --- Add Meal ---")
    name = input("Food name: ")

    protein = float(input("Protein (g): "))
    carbs = float(input("Carbs (g): "))
    fats = float(input("Fats (g): "))
    vitamins = input("Vitamins (comma separated, e.g. A,C,D): ")

    nutrition_log.append({
        "food": name,
        "protein": protein,
        "carbs": carbs,
        "fats": fats,
        "vitamins": [v.strip() for v in vitamins.split(",")]

    })

    print(f"{name} logged successfully! \n")

#Show daily nutrition summary 
def show_nutrition_summary():
    global nutrition_log #ensures we access the correct list
    if not nutrition_log:
        print("No meals logged yet. \n")
        return
    
    total_protein = sum(item["protein"] for item in nutrition_log)
    total_carbs = sum(item["carbs"] for item in nutrition_log)
    total_fats = sum(item["fats"] for item in nutrition_log)

    print("\n --- Daily Nutrition Summary ---")
    for item in nutrition_log:
        print(f"{item['food']} -> P:{item['protein']}g C:{item['carbs']}g F:{item['fats']}g")

    print("\nTotals:")
    print(f"Protein: {total_protein} g")
    print(f"Carbs: {total_carbs} g")
    print(f"Fats: {total_fats } g")


    print("\nSuggested improvements:")
    if total_protein < 100:
        print("Increase Protein intake.")
    if total_carbs < 150:
        print("Add complex carbs for energy.")
    if total_fats < 40:
        print("Healthy fats help hormones. Consider adding some.")
    print()
    input("Press Enter to return to the main menu...")

#Save nutrition data
def save_nutrition():
    with open(NUTRITION_FILE, "w") as f:
        json.dump(nutrition_log, f)
    print("Nutrition data saved!\n")



#------------------Sleep Tracking Module-----------------

SLEEP_FILE = "sleep_data.json"

#Load existing sleep data

try:
    with open(SLEEP_FILE, "r") as f:
      sleep_log = json.load(f)
except FileNotFoundError:
    sleep_log = []

#Add a sleep entry
def add_sleep():
    global sleep_log
    print("\n--- Add Sleep Entry ---")
    date = input("Date (YYYY-MM-DD): ")
    hours = float(input("Hours slept: "))
    quality = input("Sleep quality (Poor, Average, Good, Excellent): ")

    sleep_log.append({
        "date": date,
        "hours": hours,
        "quality": quality
    })

    print(f"Sleep for {date} logged successfully!\n")


#Show sleep summary

def show_sleep_summary():
    global sleep_log
    if not sleep_log:
        print("No sleep entries logged yet.\n")
        return
    total_hours = sum(entry["hours"] for entry in sleep_log)
    average_hours = total_hours / len(sleep_log)

    print("\n--- Sleep Summary ---")

    for entry in sleep_log:
        print(f"{entry['date']} {entry[hours]}, hours, Quality: {entry['quality']} ")

        print(f"\nTotal hours slept: {total_hours}")
        print(f"Average hours per entry: {average_hours:.2f}\n")
        input("Press Enter to return to the main menu...")

#Saves sleep data
def save_sleep():
    with open(SLEEP_FILE, "w") as f:
        json.dump(sleep_log, f)
    print("Sleep data saved!\n")





#Main menu
def main_menu():
    while True:
        print("=== Maverick's Gym ===")
        print("1. Add Exercise")
        print("2. Show Summary")
        print("3. Add Meal")
        print("4. Show Nutrition Summary")
        print("5. Add Sleep Entry")
        print("6. Show Sleep Summary")
        print("7. Save & Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_exercise()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            add_meal()
        elif choice == "4":
            show_nutrition_summary()
        elif choice == "5":
            add_sleep()
        elif choice == "6":
            show_sleep_summary
        elif choice == "7":
            save_data()
            save_nutrition()
            save_sleep()
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
           
