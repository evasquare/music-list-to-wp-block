from typing import TypedDict
from templates import song, spacer


class Song(TypedDict):
    level: int
    title: str
    youtube_url: str


with open('input.txt', 'r') as file:
    input = file.read()

if input == "":
    with open('input.example.txt', 'r') as file:
        input = file.read()


current_tab_level = 0
current_title = ""
output_array: list[Song] = []

for line in input.split("\n"):
    if line == "":
        continue

    splitted_by_tabs = line.split("""	""")
    while len(splitted_by_tabs) > 1:
        splitted_by_tabs = splitted_by_tabs[1:]

        if len(splitted_by_tabs) <= 1:
            refined_string = splitted_by_tabs[0].replace("- ", "", 1)

            if (refined_string.startswith("https://")):
                output_array += [Song(
                    level=current_tab_level,
                    title=current_title,
                    youtube_url=splitted_by_tabs[0].split("- ")[1]
                )]
                current_tab_level = 0
            else:
                current_title = refined_string
            break
        else:
            current_tab_level += 1
    else:
        current_tab_level = 0
        refined_string = splitted_by_tabs[0].replace("- ", "", 1)

        if (refined_string.startswith("https://")):
            output_array += [Song(
                level=current_tab_level,
                title=current_title,
                youtube_url=splitted_by_tabs[0].split("- ")[1]
            )]
        else:
            current_title = refined_string

output_string = ""

for index, item in enumerate(output_array):
    if index != 0 and index != len(output_array) - 1:
        output_string += spacer.replace("[HEIGHT]", "8px")

    using_template = str(song)
    heading_level = f"{item["level"] + 2}"
    using_template = using_template.replace(
        "[HEADING_LEVEL]", heading_level)
    using_template = using_template.replace("[SONG_NAME]", item["title"])
    using_template = using_template.replace(
        "[YOUTUBE_URL]", item["youtube_url"])
    output_string += using_template

with open("output.html", "w") as file:
    file.write(output_string)
