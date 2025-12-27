import os
import json


def load_ncert_data():
    """
    Loads NCERT science data (Classes 6–10) from JSON files.
    Returns a list of chapter dictionaries.
    """

    base_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "science"
    )
    base_path = os.path.abspath(base_path)

    chapters = []

    if not os.path.exists(base_path):
        return chapters

    for file in os.listdir(base_path):
        if file.endswith(".json"):
            file_path = os.path.join(base_path, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                    if "chapters" in data:
                        chapters.extend(data["chapters"])

            except Exception as e:
                print(f"Error loading {file}: {e}")

    return chapters
import json

def load_ncert_data():
    with open("data/ncert/science.json", "r", encoding="utf-8") as f:
        return json.load(f)
