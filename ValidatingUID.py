// Validating UID
def check_uid(uid):
    if len(uid) != 10:
        return False
    if not any(c.isupper() for c in uid):
        return False
    if not any(c.isdigit() for c in uid):
        return False
    if not all(c.isalnum() for c in uid):
        return False
    if len(set(uid)) != 10:
        return False
    return True

t = int(input().strip())
for _ in range(t):
    uid = input().strip()
    if check_uid(uid):
        print("Valid")
    else:
        print("Invalid")

        /*
        Chatgpt Prompts
        
    Me: One test case failed 
    Chatgpt :I apologize that one of the test cases failed. 
             Can you please provide the input and expected output for the failing test case? 
            This will help me identify the issue and provide a solution.
    Me:
    Input (stdin)
    2
    B1CD102354
    B1CDEF2354
    Your Output (stdout)
    Valid
    Valid
    Chatgpt provided a refined code attached in a seperate file with name - RefinedValidatingUID.py
        */
