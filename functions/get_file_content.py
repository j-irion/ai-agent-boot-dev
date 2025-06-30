from pathlib import Path


def get_file_content(working_directory, file):
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

  if not file_path.is_file():
    return f'Error: File not found or is not a regular file: "{file_path}"'

  MAX_CHARS = 10000

  with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)
  
  was_truncated = len(file_content_string) == MAX_CHARS

  if was_truncated:
    file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

  return file_content_string
