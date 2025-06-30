from pathlib import Path

def get_size(path: Path) -> int:
  if path.is_file():
    return path.stat().st_size
  elif path.is_dir():
    return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
  else:
    return 0
  

def get_files_info(working_directory, directory=None):
  working_path = Path(working_directory).resolve()
  if directory is None:
    directory_path = working_path
  else:
    directory_path = (working_path / directory).resolve()

  try:
    if not directory_path.is_relative_to(working_path):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  except ValueError:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    

  if not directory_path.is_dir():
    return f'Error: "{directory}" is not a directory'


  items = []

  for item in directory_path.iterdir():
    item_info = {
        "name": item.name,
        "is_dir": item.is_dir(),
        "size": get_size(item), 
        }
    items.append(item_info)

  out_str = ""

  for item in items:
    out_str += f"- {item["name"]}: file_size={item["size"]} bytes, is_dir={item["is_dir"]}\n"

  return out_str

