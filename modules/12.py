import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

text = "He go to college every day."

matches = tool.check(text)

print("Original:", text)

for match in matches:
    print("Problem:", match.message)
    print("Suggestion:", match.replacements)

tool.close()