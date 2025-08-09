import os, json

# This variant unlocks the recipe when the players obtains the item itself
# Suggested by @StrannikNyyan in https://github.com/costantin0/mc-no-spoiler-recipe-book/discussions/1

print(os.getcwd())
for root, dirs, files in os.walk("./recipes"):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file)
            print(filepath)
            if file.startswith("root.json"):
                os.remove(filepath)
            else:
                with open(filepath, 'w') as f:
                    json_string = json.dumps({
                    "parent": "minecraft:recipes/root",
                    "criteria": {
                        "item_obtained": {
                            "trigger": "minecraft:inventory_changed",
                            "conditions": {
                                "items": [
                                    "minecraft:{}".format(file[:len(file)-5])
                                ]
                            }
                        }
                    },
                    "requirements": [
                        [
                        "item_obtained"
                        ]
                    ],
                    "rewards": {
                        "recipes": [
                            "minecraft:{}".format(file[:len(file)-5])
                        ]
                    }
                    }, indent=4)
                    f.write(json_string)
                    