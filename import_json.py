import json

# ASCII art of an old man
ascii_art = r'''
           __
          /  \
         / ..|\
        (_\  |_)
        /  \@' 
       /     \
  _   /  `   |
  \\/  \  | _\
   \   /_ || \\_
    \____)|_) \_)
'''

print(ascii_art)

# Prompt user for the translation file and the original JSON file
translations_file = input("Enter the path to your translations file (txt): ")
json_file = input("Enter the path to your original JSON file: ")

# Read the original JSON file
with open(json_file, 'r', encoding='utf-8') as file:
    json_string = file.read()

# Parse the JSON string into a dictionary
original_dict = json.loads(json_string)

# Read the translations from the .txt file
with open(translations_file, 'r', encoding='utf-8') as file:
    translations = [line.strip() for line in file]

# Update the original dictionary with the translations
for i, key in enumerate(original_dict.keys()):
    if i < len(translations):
        original_dict[key] = translations[i]

# Convert the updated dictionary back to a JSON string
updated_json_string = json.dumps(original_dict, indent=4, ensure_ascii=False)

# Write the updated JSON string to locale.json
with open('locale.json', 'w', encoding='utf-8') as output_file:
    output_file.write(updated_json_string)

print("Updated JSON has been written to locale.json")
