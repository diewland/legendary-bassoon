import json
import os
 
TOKEN_SIZE = 500
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "This is Love"
DESC = "500 NFTs to celebrate Apetimism Launchpad (Self-Serve) with ❤️"
IMG = "https://diewland.github.io/legendary-bassoon/assets/Notes_221202_225347.jpg"
ATTRS = [
    {
      "display_type": "date", 
      "trait_type": "First Access", 
      "value": 1669977408,
    },
    {
      "trait_type": "Message Link",
      "value": "https://discord.com/channels/971042580190085160/988713397078089788/1048185857988902922",
    },
]
ENGINE = "Jigsaw Engine"

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
