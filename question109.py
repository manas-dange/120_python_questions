import re

text = "Please contact us at support@example.com or sales@example.org."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)

print("Extracted emails:", emails)
