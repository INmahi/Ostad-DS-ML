def hours_to_minutes(hours):
    return hours * 60

# Example usage:
if __name__ == "__main__":
    h = float(input("Enter hours: "))
    print(f"{h} hours is {hours_to_minutes(h)} minutes.")