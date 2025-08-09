Branch that implements [@StrannikNyyan](https://github.com/StrannikNyyan)'s suggestion from [this discussion](https://github.com/costantin0/mc-no-spoiler-recipe-book/discussions/1).

Instructions:

- Open your desired minecraft version (from the "version" folder) .jar file with a zip program;
- Extract the "recipes" folder from inside ```data\minecraft\advancements``` into the corrisponding datapack folder (where the python script is located);
- Open the terminal from inside the same folder and run the script with ```python convert_recipes.py``` (python3 if you are on Linux).

Note: make sure use the terminal to run the script from the correct directory, if (for some reason) you have a subfolder named ```recipes``` in the location you are running the script from (for example your home directory if you use VSCode with Code Runner), every JSON file present there will be overwritten!

The script will change every item recipe advancement to this:
```json
{
    "parent": "minecraft:recipes/root",
    "criteria": {
        "item_obtained": {
            "trigger": "minecraft:inventory_changed",
            "conditions": {
                "items": [
                    "minecraft:item_name"
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
            "minecraft:item_name"
        ]
    }
}
```

And that's it, the datapack is ready! It should work with future snapshots and releases if they don't change recipe related stuff in the future.
You can change the ```pack_format``` version from the ```pack.mcmeta``` file if you don't want to get a warning when selecting the datapack.
