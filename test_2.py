from ScribeLog import ConfigLog, Log, GetPathLogin, FileError

# Configure the log file
ConfigLog("Logs\yourfile.log")

# Log a message with timestamp
Log("This is a test message.")

# Log a message without timestamp
Log("Another test message.", time=False)

# Retrieve the current log file path
print(GetPathLogin())

try:
    ConfigLog("/invalid/path/to/file.txt")
except FileError as e:
    print(f"An error occurred: {e}")