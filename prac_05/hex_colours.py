"""
Hex Colour Code Lookup
Estimate: 15 minutes
Actual:   10 minutes
"""

COLOR_NAME = {"Amaranth": "#e52b50", "Aqua": "#00ffff",
              "Aureolin": "#fdee00", "Apricot": "#fbceb1",
              "Azure1": "#f0ffff", "Bittersweet": "#fe6f5e",
              "Black": "#000000", "Blond": "#faf0be",
              "Blue1": "#0000ff", "Blue2": "#0000ee"}
print(COLOR_NAME)
colour_name = input("Enter color name: ").title()
while colour_name != '':
    try:
        print(colour_name, "is", COLOR_NAME[colour_name])
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter color name: ").title()