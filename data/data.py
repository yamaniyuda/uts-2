import json
import os

def getListData() -> set:
  script_dir = os.path.dirname(__file__)
  rel_path = 'data.json'
  
  f = open(os.path.join(script_dir, rel_path))
  data = json.load(f)["colleger"]

  f.close()
  return data
  


def addData(new_data) -> None:
  script_dir = os.path.dirname(__file__)
  rel_path = 'data.json'

  with open(os.path.join(script_dir, rel_path)) as file:
    data = json.load(file)

  data["colleger"].append(new_data)

  with open(os.path.join(script_dir, rel_path)) as file:
    json.dump(data, file, indent=4)