
#  INDEXING = accessing elements of a sequence using [] (indexing operator)
#             [start : end : step]

credit_number = "1234-5678-901"

# print(credit_number[0])

# print(credit_number[0:4])

# print(credit_number[5:9])

# print(credit_number[::2])

# print(credit_number[::-1])


# last_digits = credit_number[-4:]

# print(f"XXXX-XXXX-XXXX-{last_digits}")


# EMAIL SLICER EXERCISE


email = input("enter your email: ")


index = email.index('@')

username = email[:index]
domain = email[index + 1:]

print(f"{username} and {domain}")
