class DifferencePrice:
    def __init__(self, price, payment, count_of_month):
        self.price = price
        self.payment = payment
        self.count_of_month = count_of_month
        self.total_paid_in_installments = self.payment * self.count_of_month

    def get_total_paid_in_installments(self):
        return self.total_paid_in_installments

    def get_difference(self):
        return self.total_paid_in_installments - self.price

    def get_is_correct_difference(self):
        return self.get_difference() >= 0

    @classmethod
    def compare_plans(cls, price, first_payment, first_num_of_month, second_payment, second_num_of_month):
        first_plan = cls(price, first_payment, first_num_of_month)
        second_plan = cls(price, second_payment, second_num_of_month)

        first_total = first_plan.get_difference()
        second_total = second_plan.get_difference()

        return str("First plan is better!") if first_total < second_total \
            else str("Second plan is better!") if second_total < first_total \
            else str("The plans do not have a difference!")