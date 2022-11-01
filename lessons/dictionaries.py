"""Demonstrations of dictionaries capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()


# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150
schools["UNC"] = 3500
# Print a dictionary literal syntax
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} people.")

schools.pop("Duke")

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}.")
print(schools)

# Update / Reassign a key-value pair

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")