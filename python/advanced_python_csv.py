import advanced_python_regex  
import csv

def main():
    faculty = advanced_python_regex.read_file('faculty.csv')
    emails = faculty[' email']
    with open('emails.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows([[i] for i in emails])

if __name__ == "__main__":
    main()
