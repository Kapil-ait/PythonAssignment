try:
    with open("students.txt", "r") as file, \
         open("result.txt", "w") as result_file, \
         open("error_log.txt", "w") as error_file:

        for line in file:
            record = line.strip()

            if not record:
                continue

            data = record.split(",")

            if len(data) < 4:
                error_file.write(
                    f"Error: {record} -> Marks are missing\n"
                )
                continue

            student_id, name, subject, marks = [
                item.strip() for item in data
            ]

            if not student_id:
                error_file.write(
                    f"Error: {record} -> Student ID is missing\n"
                )
                continue

            if not name:
                error_file.write(
                    f"Error: {record} -> Student Name is missing\n"
                )
                continue

            if not subject:
                error_file.write(
                    f"Error: {record} -> Subject is missing\n"
                )
                continue

            if not marks:
                error_file.write(
                    f"Error: {record} -> Marks are missing\n"
                )
                continue

            try:
                marks = float(marks)
            except ValueError:
                error_file.write(
                    f"Error: {record} -> Marks must be numeric\n"
                )
                continue

            if not 0 <= marks <= 100:
                error_file.write(
                    f"Error: {record} -> Marks must be between 0 and 100\n"
                )
                continue

            if marks >= 90:
                result = "Excellent"
            elif marks >= 75:
                result = "Very Good"
            elif marks >= 60:
                result = "Good"
            elif marks >= 40:
                result = "Pass"
            else:
                result = "Fail"

            marks = int(marks) if marks.is_integer() else marks

            result_file.write(
                f"{student_id} - {name} - {subject} - "
                f"{marks} - {result}\n"
            )

    print("Student result processing completed successfully.")
    print("Valid records have been written to result.txt")
    print("Invalid records have been written to error_log.txt")

except FileNotFoundError:
    print("Error: students.txt file not found.")

except OSError as e:
    print("File handling error:", e)