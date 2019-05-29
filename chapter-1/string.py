# Normal string
firstName = "Thinh"
middleName = "Duc"
lastName = "Nguyen"

fullName = firstName + " " + middleName + " " + lastName;

print("Full Name: " + fullName);

# Multiple line string
oneLine = "This is the first example of\
multiple line string";

multipleLineWithLn = """This is the second example of\
multiple line string"""

print(oneLine);
print(multipleLineWithLn);

# Slice string
startIndex = 0
endIndex = 5    # doesn't count this index

print("Sliced (First Name): " + fullName[startIndex:endIndex])


