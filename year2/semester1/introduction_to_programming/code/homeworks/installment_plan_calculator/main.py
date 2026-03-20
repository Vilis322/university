from plan_calculator import DifferencePrice


def user_input(input_message="message", error_message="error message"):
    while True:
        try:
            value = float(input(f"\nPlease, enter {input_message}:\n").replace(",", ".").strip())
            if value < 0:
                print(f"\n{input_message.capitalize()} cannot be negative.\nPlease enter a positive numerical value!")
                continue
            return value
        except ValueError:
            print(f"\n{error_message}\nPlease, enter a valid numerical value!\n")


def get_plan_details(price):
    while True:
        monthly_payment = user_input(input_message="the monthly payment", error_message="Invalid input!")
        num_of_month = user_input(input_message="the number of months", error_message="Invalid input!")

        plan = DifferencePrice(price, monthly_payment, num_of_month)

        if plan.get_is_correct_difference():
            return plan
        else:
            print("The plan has a negative difference! Please enter the details again.")


def main():
    total_price = user_input(input_message="the total price", error_message="Invalid input!")

    print("\nEnter details for the first installment plan:")
    first_plan = get_plan_details(total_price)

    print(f"\nThe overpayment for the first plan is: {first_plan.get_difference()}\n")
    print("Enter details for the second installment plan:")
    second_plan = get_plan_details(total_price)

    print(f"\nThe overpayment for the second plan is: {second_plan.get_difference()}\n")
    result = DifferencePrice.compare_plans(total_price, first_plan.payment, first_plan.count_of_month,
                                           second_plan.payment, second_plan.count_of_month)
    print(result)


if __name__ == "__main__":
    main()
