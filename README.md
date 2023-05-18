Instructions:

- Open your desired minecraft version (from the "version" folder) .jar file with a zip program;
- Extract the "recipes" folder from inside ```data\minecraft\advancements``` into the corrisponding datapack folder;
- Open the terminal from the datapack folder (where the python script is located), open a terminal and run the script with ```python convert_recipes.py``` (python3 if you are on Linux).

Note: make sure use the terminal to run the script from the correct directory, if you have a subfolder named ```recipes``` in the location you are executing the script from (for example your home directory if you open the script directly with VScode and use Code Runner), every .json file present there will be overwitten!

The 1.19.4 script will change every item recipe to this:
```
   {
   "parent":"minecraft:recipes/root",
   "criteria":{
      "was_crafted":{
         "conditions":{
            "items":[
               {
                  "items":[
                     "minecraft:item_name"
                  ]
               }
            ]
         }
      }
   },
   "requirements":[
      [
         "was_crafted"
      ]
   ],
   "rewards":{
      "recipes":[
         "minecraft:item_name"
      ]
}
```
The 23w16a script will change them to this:
```
{
    "parent": "minecraft:recipes/root",
    "criteria": {
        "was_crafted": {
            "trigger": "minecraft:recipe_crafted",
            "conditions": {
                "recipe_id": "minecraft:item_name"
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
            "minecraft:item_name"
        ]
    }
}
```

And that's it, the datapack is ready! The 23w16a version should work with future snapshots and releases if they don't change recipe related stuff in the future, and the 1.19.4 version should also work on older versions. You can change the ```pack_format``` version from the ```pack.mcmeta``` file if you don't want to get a warning when selecting the datapack.
