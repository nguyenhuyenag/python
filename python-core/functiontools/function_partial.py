from functools import partial

def target_func(arg_one, arg_two):
    print(f"arg_one = {arg_one}, arg_two = {arg_two}")

partial_one = partial(target_func, arg_two="World!")
partial_two = partial(target_func, arg_one="Love")

partial_one(arg_one="Hello")
partial_two(arg_two="Python")
