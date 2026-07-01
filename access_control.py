permissions = {
    "Admin":["read","write"],
    "User":["read"],
    "Auditor":["view_logs"]
}

def check_permission(role, action):
    return action in permissions.get(role, [])

