from pathlib import Path

def write_file(working_directory, file, content):
  working_path = Path(working_directory).resolve()
  if file is None:
    file_path = working_path
  else:
    file_path = (working_path / file).resolve()

  try:
    if not file_path.is_relative_to(working_path):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
  except ValueError:
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

  file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directories exist
  with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

  return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
