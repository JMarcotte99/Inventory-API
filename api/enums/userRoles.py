from enum import Enum

class UserRoles(str, Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"