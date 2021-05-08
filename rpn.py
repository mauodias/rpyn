import math
import operator

binary_ops = {"+":operator.add, "-":operator.sub, "*":operator.mul ,"/":operator.truediv, "**":operator.pow, "//":operator.floordiv, "%":operator.mod}
unary_ops = {"abs":operator.abs, "sqrt":math.sqrt}
reduce_ops = {"sum": sum}


def run():
    stack = []
    while True:
        cmd = input()
        if cmd.lower() in reduce_ops.keys():
            f = reduce_ops[cmd.lower()]
            stack = [f(stack)]
        elif cmd.lower() in unary_ops.keys():
            f = unary_ops[cmd.lower()]
            value = stack.pop()
            stack.append(f(value))
        elif cmd.lower() in binary_ops.keys():
            f = binary_ops[cmd.lower()]
            b = stack.pop()
            a = stack.pop()
            stack.append(f(a,b))
        else:
            try:
                stack.append(float(cmd))
            except:
                print("Invalid input")
        print(stack)

if __name__ == "__main__":
    run()
