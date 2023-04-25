import json
import settings

mode = ""
while True:
  mode = input("Client or Server? (c/s)")
  if mode in "csCS" and bool(mode):
    break

path = ""
folder = ""
if mode in "cC": 
  path = settings.clientPath
  folder = "Client"
elif mode in "sS": 
  path = settings.serverPath
  folder = "Server"

print("Generating manifest from " + path + "/config.json")
config = json.loads(open(path + "/config.json", "r", encoding="utf8").read())

loaderType = config["loader"]["loaderType"]
mcVersion = config["loader"]["mcVersion"]
loaderVersion = config["loader"]["loaderVersion"]

packName = "Dirt Eaters Modpack"
packVersion = "1.1"
packAuthor = "niraqw15"

manifest = {
  "minecraft": {
    "version": mcVersion,
    "modLoaders": [
      {
        "id": loaderType + loaderVersion[len(mcVersion):],
        "primary": True
      }
    ]
  },
  "manifestType": "minecraftModpack",
  "manifestVersion": 1,
  "name": packName,
  "version": packVersion,
  "author": packAuthor,
  "files": [],
  "overrides": "overrides"
}

files = manifest["files"]

for modInfo in config["mods"]:
    if "projectID" in modInfo and "fileID" in modInfo:
      if ".disabled" not in modInfo["fileName"]:
        mod = {
          "fileName": modInfo["fileName"],
          "projectID": modInfo["projectID"],
          "fileID": modInfo["fileID"]
        }
        files.append(mod)

manifestFile = open(folder + "/manifest.json", "w")
manifestFile.write(json.dumps(manifest, indent=4))
manifestFile.close()

print("Finished writing to " + folder + "/manifest.json")