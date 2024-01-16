import pandas as pd
import toml
import glob
import inquirer
# TODO: Auto search file ending with .csv

files= glob.glob('*.csv')
answer = [inquirer.List("path",message="Select the input file",choices=files),]
input_file_path = inquirer.prompt(answer)["path"]
with open("settings.toml",'r') as f:
    settings = toml.load(f)

no_of_cards = settings["settings"]["no_of_cards"]
output_file_path = settings["settings"]["output_file_path"]

if output_file_path == '':
    output_file_path = f"top{no_of_cards}raidCards.csv"
df = pd.read_csv(input_file_path)

# Create a new column with the sum of specified columns
df['sumStats'] = df[['hp', 'defense', 'attack', 'speed']].sum(axis=1)

# Sort the DataFrame in descending order based on the new column
df = df.sort_values(by='sumStats', ascending=False)

# Display the top rows
raidCards = df.head(no_of_cards)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print(f"Done!. Check {output_file_path} for the raid cards")
print(raidCards)

