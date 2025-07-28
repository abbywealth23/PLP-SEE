admins = {"wealth", "Ayobami"}
editors = {"Ayobami" , "Opeyemi"}

all_users = admins.union(editors)
print("All User" , all_users)
both_roles = admins.intersection(editors)
print("users with both roles:", both_roles)

admin_only = admins.difference(editors)
print("Admin Only:" , admin_only)