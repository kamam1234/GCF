def multiline_input():
    result = input("Enter multiple lines of text (press Ctrl+D or Ctrl+Z to stop): ")
    while True:
        line = input()
        result += " " + line
        if line == '':
            break
    return result

print(multiline_input())