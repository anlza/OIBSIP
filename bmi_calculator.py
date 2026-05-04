import csv
import matplotlib.pyplot as plt


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

try:
    print("🧮 BMI Calculator")
    print("----------------------")

  
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meters): "))

    if weight <= 0 or height <= 0:
        print("\n Values must be positive.")
    else:
        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print("\n Result")
        print("----------------------")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

        with open("bmi_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([weight, height, round(bmi, 2), category])

        print("\n Data saved successfully!")

        
        choice = input("\nDo you want to see BMI history graph? (y/n): ").lower()

        if choice == "y":
            bmi_values = []

            with open("bmi_data.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    bmi_values.append(float(row[2]))

            plt.plot(bmi_values)
            plt.title("BMI History")
            plt.xlabel("Entry")
            plt.ylabel("BMI")
            plt.show()

except ValueError:
    print("\n Invalid input. Please enter numbers only.")
except Exception as e:
    print("\n Unexpected error:", e)