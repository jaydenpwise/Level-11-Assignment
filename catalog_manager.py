# Level #11 Assignment - Video Game Catalog Manager
# IS 303 - Hilton
# Author: jaydenpwise
#
# Reads video_games_raw.csv, lets the user inspect and update one game's
# status, flags recommended games, and saves the result to
# video_games_cleaned.csv. The original CSV file is never modified.

import pandas as pd

RAW_FILE = "video_games_raw.csv"
CLEANED_FILE = "video_games_cleaned.csv"

# Read the CSV file using Pandas
df = pd.read_csv(RAW_FILE)

print("VIDEO GAME CATALOG MANAGER")
print()

# Ask the user for a specific row number to inspect (keep asking until valid)
while True:
    row_input = input("Enter a row number to inspect: ")
    try:
        row_number = int(row_input)
    except ValueError:
        print(f"Please enter a whole number between 0 and {len(df) - 1}.")
        continue
    if 0 <= row_number < len(df):
        break
    print(f"Please enter a row number between 0 and {len(df) - 1}.")

# Use .iloc[] to access the selected game by its position
selected_game = df.iloc[row_number]

print()
print("Selected Game:")
print(f"Title: {selected_game['Title']}")
print(f"Platform: {selected_game['Platform']}")
print(f"Genre: {selected_game['Genre']}")
print(f"Rating: {selected_game['Rating']}")
print(f"Current Status: {selected_game['Status']}")

# Ask the user to enter a new status for that game
print()
print("Enter a new status:")
new_status = input().strip()

# Use .at[] to change that one specific value
# (.at[] works with index labels, so look up the label for this position)
row_label = df.index[row_number]
df.at[row_label, "Status"] = new_status

# Add a Recommended column, defaulting every game to "No"
df["Recommended"] = "No"

# Use .loc[] to change multiple rows: games rated at least 8 that cost $40 or less
df.loc[(df["Rating"] >= 8) & (df["Price"] <= 40), "Recommended"] = "Yes"

# Use .query() to display the recommended games
recommended_games = df.query("Recommended == 'Yes'")

print()
print("Recommended Games:")
print(recommended_games[["Title", "Platform", "Price", "Rating"]])

# Save the updated data to a new file so the original stays unchanged
df.to_csv(CLEANED_FILE, index=False)

print()
print("The catalog has been updated.")
print(f"Saved as {CLEANED_FILE}.")
