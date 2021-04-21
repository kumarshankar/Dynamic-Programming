from collections import deque
no_of_chars = 256

def findSubstring(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)
    if len_text < len_pattern :
        print("No such window exists")
        return ""    
    hash_pat = [0] * no_of_chars
    hash_text = [0] * no_of_chars

    # Store occurence of characters of pattern
    for i in range(0, len_pattern):
        hash_pat[ord(pattern[i])] += 1
    
    start, start_index, min_length = 0, -1, float('inf')

if __name__ == "__main__":
    string = "this is a test string"
    pat = "tist"
    findSubstring(string, pat)
