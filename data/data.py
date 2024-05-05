import json
import os

def getListData() -> set:
  script_dir = os.path.dirname(__file__)
  rel_path = 'data.json'
  
  f = open(os.path.join(script_dir, rel_path))
  data = json.load(f)["colleger"]

  f.close()
  return data
  