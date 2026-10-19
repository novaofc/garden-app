# Garden Advice Program
# Asks the user for the current season and the type of plant they are
# growing, then prints simple gardening advice based on their answers.

# Ask the user for the season and plant type.
# .strip() removes any extra spaces and .lower() converts the text to
# lowercase, so inputs like " Summer" still match the checks below.
season = input("Enter the season (summer or winter): ").strip().lower()
plant_type = input("Enter the plant type (flower or vegetable): "
                   ).strip().lower()

# Start with an empty string; advice is added to it in the sections below.
advice = ""

# Season advice:
# Add a tip based on the season. If the season isn't recognised,
# add a fallback message so the user still gets a response.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Plant type advice:
# Add a tip based on the plant type, with a fallback for unknown types.
# The season tip ends with "\n", so this tip appears on a new line.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Output:
# Display the combined advice to the user.
print(advice)

# TODO: Examples of possible features to add:
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
