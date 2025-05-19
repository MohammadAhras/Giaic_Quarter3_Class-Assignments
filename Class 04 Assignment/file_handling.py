filename = "data.txt"

# Write names to file
def write_names():
    with open(filename, "w") as file:
        file.write("Ali\nSara\nHamza\nAyesha\n")
    print("✅ Names written to file.\n")

# Read names from file
def read_names():
    with open(filename, "r") as file:
        content = file.read()
    print("📄 File Contents:\n", content)

# Append names
def append_names():
    with open(filename, "a") as file:
        file.write("Zainab\nBilal\n")
    print("✅ Names appended to file.\n")

write_names()
read_names()
append_names()
read_names()
