with open("entry_error.html", "r", encoding="utf-8") as f:
    content = f.read()
    if "Exception Value:" in content:
        start_index = content.find("Exception Value:")
        # Print next 500 chars to cover the value
        print(content[start_index:start_index+500])
    elif "exception_value" in content:
        start_index = content.find("exception_value")
        print(content[start_index:start_index+500])
    else:
        print("Exception value marker not found.")
        # Print checking for other keywords
        print("IntegrityError?" + str("IntegrityError" in content))
        print("AttributeError?" + str("AttributeError" in content))
