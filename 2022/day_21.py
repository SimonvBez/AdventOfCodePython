from operator import add, sub, mul, floordiv, eq


class Expression:
    @staticmethod
    def make_expression(expr_str):
        try:
            return Number(int(expr_str))
        except ValueError:
            left_str, op_str, right_str = expr_str.split(" ")
            match op_str:
                case "+":
                    op = add
                case "-":
                    op = sub
                case "*":
                    op = mul
                case "/":
                    op = floordiv
                case _:
                    op = eq
            return ExpressionBinary(left_str, right_str, op)

    def find_path_to_name(self, name):
        return None

    def get_result(self):
        pass


class ExpressionBinary(Expression):
    def __init__(self, left, right, op):
        self.left_str = left
        self.right_str = right
        self.left = None
        self.right = None
        self.op = op

    def find_path_to_name(self, name):
        if self.left is name:
            return "<"
        if self.right is name:
            return ">"
        if result := self.left.find_path_to_name(name):
            return "<" + result
        if result := self.right.find_path_to_name(name):
            return ">" + result
        return None

    def calculate_other(self, desired_result, side_str):
        side, rest = side_str[0], side_str[1:]
        if side == "<":
            side_to_calculate = self.left
            known_side = self.right
        else:
            side_to_calculate = self.right
            known_side = self.left
        known_side_result = known_side.get_result()

        if self.op is add:
            required_value = desired_result - known_side_result
        elif self.op is sub:
            if side_to_calculate is self.left:
                required_value = desired_result + known_side_result
            else:
                required_value = known_side_result - desired_result
        elif self.op is mul:
            required_value = desired_result // known_side_result
        elif self.op is floordiv:
            if side_to_calculate is self.left:
                required_value = desired_result * known_side_result
            else:
                required_value = known_side_result / desired_result
        else:  # self.op must be eq
            required_value = known_side_result

        if rest:
            return side_to_calculate.calculate_other(required_value, rest)
        else:
            return required_value

    def get_result(self):
        left = self.left.get_result()
        right = self.right.get_result()
        return self.op(left, right)


class Number(Expression):
    def __init__(self, num):
        self.num = num

    def get_result(self):
        return self.num


def main():
    variables = {}
    with open("day_21_input", "r") as f:
        for line in (x.strip() for x in f):
            variable, expression = line.split(": ")
            variables[variable] = Expression.make_expression(expression)

    for expression in variables.values():
        if isinstance(expression, ExpressionBinary):
            expression.left = variables[expression.left_str]
            expression.right = variables[expression.right_str]

    root = variables["root"]

    print(root.get_result())

    root.op = eq
    me = variables["humn"]
    path = root.find_path_to_name(me)
    print(root.calculate_other(1, path))


if __name__ == "__main__":
    main()
