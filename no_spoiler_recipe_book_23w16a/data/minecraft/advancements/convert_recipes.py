import os, json

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
                        "was_crafted": {
                            "trigger": "minecraft:recipe_crafted",
                            "conditions": {
                            "recipe_id": "minecraft:{}".format(file[:len(file)-5])
                            }
                        }
                        },
                    "requirements": [
                        [
                        "was_crafted"
                        ]
                    ],
                    "rewards": {
                        "recipes": [
                        "minecraft:{}".format(file[:len(file)-5])
                        ]
                    }
                    }, indent=4)
                    f.write(json_string)
                    