  /* Chatgpt prompt :
        
        The issue is with the condition if len(set(uid)) != 10: in the check_uid function. 
        The purpose of this condition is to check if there are any repeating characters in the UID, 
        but it is checking if the number of unique characters in the UID is not 10, which is incorrect. 
        To correctly check for repeating characters, we can use a set to keep track of the characters we have seen so far,
        and return False if we have already seen a character. Here's the corrected code:
    
    */


def check_uid(uid):
    if len(uid) != 10:
        return False
    if not any(c.isupper() for c in uid):
        return False
    if not any(c.isdigit() for c in uid):
        return False
    if not all(c.isalnum() for c in uid):
        return False
    seen = set()
    for c in uid:
        if c in seen:
            return False
        seen.add(c)
    return True

t = int(input().strip())
for _ in range(t):
    uid = input().strip()
    result = "Valid" if check_uid(uid) else "Invalid"
    print(result)

    
  
