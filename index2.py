import csv
from data import data


def add_country_code(numbers):
    return ["+91" + number for number in numbers]

def save_to_csv(unique_numbers, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in unique_numbers:
            writer.writerow([number])

def main():
    # Example list of numbers
    numbers = [entry["phoneNumber"]["$numberLong"] for entry in data]
    
    # Add country code to each number
    numbers_with_country_code = add_country_code(numbers)
    
    # Get unique numbers
    unique_numbers = list(set(numbers_with_country_code))
    
    # Save unique numbers to a CSV file
    save_to_csv(unique_numbers, "unique_numbers.csv")

if __name__ == "__main__":
    main()
