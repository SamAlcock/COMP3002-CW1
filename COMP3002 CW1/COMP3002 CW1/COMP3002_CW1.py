def pallindrome_q1a(word):
    if len(word) == 1:
        return True
    if word[0] == word[-1]:
        return pallindrome_q1a(word[1:-1])
    
    return False

word = "madam"
if pallindrome_q1a(word):
    print(word + " is pallindrome")
else:
    print(word + " is not pallindrome")
