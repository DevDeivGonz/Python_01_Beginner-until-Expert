
"""

What Are Sets in Python?

A set is a built-in data structure in Python that represents an unordered collection of unique elements. Sets are useful when you need to store items without duplicates and when the order of items does not matter.
Characteristics of Sets:

    Unordered: The elements do not have a specific order.
    Unique: Duplicate elements are automatically removed.
    Mutable: You can add or remove items from a set after creation.

"""

# List of email addresses with duplicates

email_list = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com"
]

# Convert list to set to remove duplicates
unique_emails = set(email_list)

# Print the unique email addresses
print("Unique email addresses:", unique_emails)
