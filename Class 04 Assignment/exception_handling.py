def divide_100():
    try:
        num = int(input("Enter a number to divide 100: "))
        result = 100 / num
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")
    except ValueError:
        print("❌ Error: Please enter a valid number.")
    else:
        print("✅ Result:", result)
    finally:
        print("🔁 Division attempt completed.\n")

divide_100()


def check_positive(num):
    try:
        if num < 0:
            raise ValueError("Negative number is not allowed.")
        print("✅ Number is positive.")
    except ValueError as e:
        print("❌ Exception:", e)
    finally:
        print("🔚 Checked number.")

check_positive(-7)
