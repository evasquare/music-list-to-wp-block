from typing import TypedDict
from templates import song, spacer


class Song(TypedDict):
    level: int
    title: str
    url: str


with open('input.txt', 'r') as file:
    input = file.read()

if input == "":
    with open('input.example.txt', 'r') as file:
        input = file.read()


# Prase the list
previous_tab_level = 0
previous_title = ""
output_array: list[Song] = []

for line in input.split("\n"):
    if line == "":
        continue

    # Check tab level and text
    splitted_by_tabs = line.split("""	""")
    new_tab_level = 0
    new_title = ""

    for item in splitted_by_tabs:
        if (item != ""):
            new_title = splitted_by_tabs[-1].replace("- ", "", 1)
            break
        else:
            new_tab_level += 1

    # Check URL
    if (new_title.startswith("https://")):
        if (new_tab_level <= previous_tab_level):
            raise Exception("Invalid syntax...")
        else:
            output_array.append(Song(
                level=new_tab_level - 1,
                title=previous_title,
                url=new_title
            ))

    previous_tab_level = new_tab_level
    previous_title = new_title


# Use templates
output_string = ""

for index, item in enumerate(output_array):
    if index != 0:
        output_string += spacer.replace("[HEIGHT]", "8px")

    using_template = str(song)
    heading_level = f"{item["level"] + 2}"
    using_template = using_template.replace(
        "[HEADING_LEVEL]", heading_level)
    using_template = using_template.replace("[SONG_NAME]", item["title"])
    using_template = using_template.replace(
        "[YOUTUBE_URL]", item["url"])
    output_string += using_template

with open("output.html", "w") as file:
    file.write(output_string)
