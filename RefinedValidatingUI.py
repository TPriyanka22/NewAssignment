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
    result = "Valid" if check_uid(uid) else "Invalid"
    print(result)
