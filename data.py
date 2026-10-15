import csv
from actions import students

def export_students():
    if not students:
        print("No students to export.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "section",
                "spanish",
                "english",
                "social_studies",
                "science"
            ]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Students exported successfully!")

def import_students():
    print("Importing students from CSV...")

    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

            row["spanish"] = float(row["spanish"])
            row["english"] = float(row["english"])
            row["social_studies"] = float(row["social_studies"])
            row["science"] = float(row["science"])

            if not any(
                student["name"].strip().lower() == row["name"].strip().lower()
                and student["section"].strip().lower() == row["section"].strip().lower()
                for student in students
            ):
                students.append(row)
                print("Student imported successfully!")
            else:
                print("Student already exists. Skipping duplicate.")
