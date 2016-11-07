def palindrome(str):
    minified = ""
    for char in str:
        if char != " ":
            minified += char
    minified = minified.lower()
    reversed = ""
    for i in range(len(minified) - 1, -1, -1):
        reversed += minified[i]
    
    return minified == reversed

def main():
   return

if __name__ == '__main__':
    main()
