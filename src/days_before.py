from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate 90 days before today
days_before = today - timedelta(days=90)

# Format the result as a string
result = days_before.strftime("%d-%b-%Y")

print("90 days before today:", result)
