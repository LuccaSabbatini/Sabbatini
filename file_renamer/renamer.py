# Imports
import os

# Renamer function definition:
def renamer(origin, destiny, newname):
    i = 1 # Renamer index.

    for filename in os.listdir(origin): # Loop sweeping through original directory unrenamed files.
        frmt = filename.split(".")[-1] # Stores current file extension in iteration being renamed.
        
        # Storing source directory and destiny plus new file name directory in variables.
        src = origin + '/' + filename
        dst = destiny + '/' + newname + '(' + str(i) + ')' + '.' + frmt

        os.rename(src, dst) # Renaming file through os.rename() function.
        
        i += 1 # Incrementing renamer index.

    print("\nSuccess!!!\n\n") # Success message.

print("\n__File Renamer__\n") # Start-up message.

newfilename = str(input("New Standard Name: ")) # Fetching new file for renaming process.
standard = str(input("Use standard directories? [ y / n ]: ")) # Use renamer standard directory folders or use other directories.

# Storing directories to be used in renaming process in variables.
if standard == 'y': # User wants to use standard directories.
    originalDir = 'origin'
    finalDir = 'destiny'
else: # User wants to use custom directories.
     originalDir = str(input("Origin Directory: "))
     finalDir = str(input("Final Directory: "))

renamer(originalDir, finalDir, newfilename) # renamer() call.
