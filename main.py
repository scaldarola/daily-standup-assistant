import os
import sys
from datetime import datetime
from datetime import date
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

llm = Ollama(
    model="llama3", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

commits_dir = os.getenv('COMMITS_DIRECTORY')

if not commits_dir:
    print("COMMITS_DIRECTORY is not set. Exiting the program.")
    sys.exit(1)  

def get_newest_file_content(directory):
  """
  This function finds the newest file (based on creation time) in the specified directory 
  and returns its content.

  Args:
      directory: The path to the directory to search.

  Returns:
      The content of the newest file as a string, or None if no files are found or an error occurs.
  """
  newest_file = None
  newest_file_time = None
  for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
      file_stats = os.stat(file_path)
      creation_time = datetime.fromtimestamp(file_stats.st_ctime)
      if newest_file_time is None or creation_time > newest_file_time:
        newest_file = file_path
        newest_file_time = creation_time
  
  if newest_file:
    try:
      with open(newest_file, 'r') as file:
        return file.read()
    except FileNotFoundError:
      return None
    except Exception as e:
      print(f"Error reading file: {newest_file} - {e}")
      return None
  else:
    return None

content = get_newest_file_content(commits_dir+"/commits")

result = llm("I am a DevOps Engineer in a team that we do development of kubernetes clusters tooling and mainteinance. One of our ways of working, is to summarise the work done each day in a written standup message. Most of my work is done via github repositories, so commit messages log most of the work that I do every single day. I am gathering all commits from every single day on a text file, and I'm going to share them with you. I need you to summarise for every commit provided, the content in a one liner, and share them as bullet points for me. Some considerations about the content I'll provide: every commit is separated by a new line and this characters: --- so it's easy for you to separate them. Also, please only reply with the bullet points and nothing else. Beware of duplicate entries, i don't need them. Also, filter out any commit message that has the word fixup ahead. The content of commits is: " + content)

def write_string_to_file(content, directory):
  """
  This function writes a string to a file with the current date in the format dd-mm-yyyy.txt.

  Args:
      content: The string content to be written to the file.
      directory: The directory path where the file will be saved.
  """
  today_date = date.today().strftime("%d-%m-%Y")
  file_path = os.path.join(directory, f"{today_date}.txt")

  try:
    with open(file_path, 'w') as file:
      file.write(content)
      print(f"String written to file: {file_path}")
  except FileNotFoundError:
    os.makedirs(directory, exist_ok=True)  
    write_string_to_file(content, directory) 
  except Exception as e:
    print(f"Error writing to file: {file_path} - {e}")

write_string_to_file(result, commits_dir+"/result")
