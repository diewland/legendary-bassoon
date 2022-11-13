import json, glob, random
from datetime import datetime
from pprint import pprint as pp

NAME = "Just Steak 🥩"
DESC = "To Proof 7$ NFTs are possible. Pick your favorite dish. Allez Cuisine!"
IMG = "https://diewland.github.io/legendary-bassoon/just-steak/assets/{}"
ENGINE = "Jigsaw Engine"

SRC_PATH = "./assets/*.png"
OUTPUT_DIR = "./json"
SHUFFLE_TIME = 99

# extract raw data
raw = []
for file in glob.glob(SRC_PATH):
    raw.append(file.split("/")[2])
    
# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(raw)

#pp(raw)
#exit()

# build chunk
chunk = []
for id, img in enumerate(raw):
    # debug
    #print(id, img)

    # template
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        #{
        #  "trait_type": "Scene",
        #  "value": "***",
        #},
      ],
      "compiler": ENGINE,
    }

    # update data
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(img)
    #metadata["attributes"][0]["value"] = scene

    # add to chunk
    chunk.append(metadata)

#pp(chunk)
#exit()

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
