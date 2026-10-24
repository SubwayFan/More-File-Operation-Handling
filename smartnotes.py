# ================================
# SMART NOTES ORGANIZER
# ================================

# ---------- SETUP (given to you) ----------
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")


# ---------- PART 1: read(40) ----------
print("\nPART 1: Preview with read(40)")
# YOUR CODE HERE
# Open class-notes.txt in read mode, print the first 40 characters, close it.
file = open("class-notes.txt", "r")
file.writelines(sample_notes)
file.close()

# ---------- PART 2: readlines() ----------
print("\nPART 2: readlines()")
# YOUR CODE HERE
# Open the file, use readlines() to get a list, close the file.
# Print how many lines there are.
# Then print each line with its number, like:  1 -> IMPORTANT: ...
# Use .strip() so you do not get blank lines between them.
numoflines = file.readlines()
file.close()
print("You have ", len(numoflines), " lines.")


# ---------- PART 3: loop line by line ----------
print("\nPART 3: Loop line by line")
# YOUR CODE HERE
# Open the file again and use  for line in file:  to print each line.
# Print it as:  Reading: <the line>


# ---------- PART 4: filter with a condition ----------
print("\nPART 4: Filter with a condition")
# YOUR CODE HERE
# Loop through the file. If the line starts with "SKIP", print  Skipped: <line>
# Otherwise print  Kept: <line>
# Count how many you kept and how many you skipped, and print the totals at the end.
word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skipping -->", line.strip())
        wordsskipped = wordsskipped + 1
    else:
        print("Keeping -->", line.strip())
        wordskept = wordskept + 1
file.close()
print("Words kept: " + wordskept )
print("Words skipped: " + wordsskipped)



# ---------- PART 5: copy selected lines ----------
print("\nPART 5: Copy selected lines to a new file")
# YOUR CODE HERE
# Read all the lines into a list.
# Open organized-notes.txt in WRITE mode.
# Write only the lines that start with "IMPORTANT" or "TODO".
# Close both files. Print how many lines you copied.
linescopied = 0
file = open("organized-notes.txt", "r")
for line in file:
    if line.startswith("important"):
        print(line)
        linescopied = linescopied + 1
    elif line.startswith("TODO"):
        print(line)
        linescopied = linescopied + 1
    else:
        print("Skipping -->", line.strip())
        
file.close()
print("Lines copied: " + linescopied )

# ---------- PART 6: show the result ----------
print("\nPART 6: Organized notes")
# YOUR CODE HERE
# Open organized-notes.txt and print ev

#Copy old lines to a new file
file = open("class-notes", "r")
lines = file.readlines()
file.close()
#This will automatically creaet and open a new text file
out = open("organized-notes.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Updated information.txt")