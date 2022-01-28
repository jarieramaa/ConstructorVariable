import random


class MyClass:
    """Trying to figure out if mutable object as a constructor
    parameter is causing troubles. So far there is no problems."""

    def __init__(self, name) -> None:
        self.my_variable = []  # IS THIS CAUSING TROUBLES??
        self.name = name

    def add_item(self):
        message = self.name + ", " + str(random.randint(0, 1000))
        self.my_variable.append(message)

    def variable_id(self):
        return id(self.my_variable)

    def print_id(self):
        print(self.name, "my variable id is:", id(self.my_variable))

    def print_list(self):
        print(self.name, "list:", self.my_variable)


def automatic_test():
    list_of_instances = []
    list_of_variable_ids = []
    for i in range(0, 2000):
        instance_name = "inst_" + str(i)
        instance = MyClass(instance_name)
        list_of_instances.append(instance)
        instance_variable_id = id(instance.variable_id)
        if instance_variable_id in list_of_variable_ids:
            print("\n\nSAME ID EXISTS ALREADY!!!")
            print("instance variable_id:", instance_variable_id)
            print("list of variable ID's:", list_of_variable_ids)
            break
        list_of_variable_ids.append(instance_variable_id)
    print(list_of_variable_ids)


automatic_test()


#for i in list_of_instances:
def super_simple_solution():
    inst_1 = MyClass("instance_1")
    inst_2 = MyClass("instance_2")
    inst_3 = MyClass("instance_3")
    print("=" * 100)
    inst_1.print_id()
    inst_2.print_id()
    inst_3.print_id()
    inst_1.add_item()
    inst_1.add_item()
    inst_1.add_item()
    inst_2.add_item()
    inst_2.add_item()
    inst_2.add_item()
    inst_3.add_item()
    inst_3.add_item()
    inst_3.add_item()
    print("=" * 100)
    inst_1.print_list()
    inst_2.print_list()
    inst_3.print_list()
