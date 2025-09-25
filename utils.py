"""
    utils.py
    Author: Joe Scott
    Date: 09/25/2025
    
    Purpose: Creates a fancy title for your programs when imported.
"""

def main():
    print(title("Print title test!"))
    print(UnderLN("Print underlined title test!"))

# Box title
def title(statement):
    
    # Get length of the statement string variable
    text_length = len(statement)

    #Create and initialize title.
    result = ""
    result += " ___" + "_" * text_length + "_\n"
    result += "|  " + " " * text_length + "  |\n"
    result += "|  " + statement + "  |\n"
    result += "|__" + "_" * text_length + "__|\n"

    return result

# Underline Title
def UnderLN(statement):
    # Get length of the statement string variable
    text_length = len(statement)

    # Create a title
    result = ""
    result += statement
    result += "\n"
    result += text_length * "-"

    return result

# Run in this file.
if __name__ == "__main__":
    main()
