users_file = open(r"users.txt", "r")

with open("users.txt") as file:
    users = [line.rstrip() for line in file]

print(users)

users_file = open(r"users.txt", "r")
users = users_file.readlines()
users_file.close()

for i in range(0, len(users) - 1):
    users[i] = users[i].replace("\n", '')

users_data = {
    'usernames': users[0:4],
    'emails': users[5:9],
    'birthdates': users[10:15]
}

print(users_data)
