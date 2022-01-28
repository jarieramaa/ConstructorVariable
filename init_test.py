"""During Hangman programming demo it was told that you
should not create empty list as a constructor attribute. That's 
because, other instances of that same class might refer to that same 
object as well.
I wanted to check this. I believe that they would have noticed this
in Google if it's true. Pylint doesn't give any warnings about it.
"""

from typing import List
import os

os.system('cls' if os.name == 'nt' else 'clear')


class MyClass:
    """Trying to figure out if mutable object as a constructor
    variable is causing troubles."""

    def __init__(self, name: str) -> None:
        """Constructor with empty list attribute"""
        self.my_list = []  # <------- IS THIS CAUSING TROUBLES??
        self.name = name

    def add_item_to_list(self) -> None:
        """Idea is that every instance adds themselves to the
        list after all instances has been created. In this test this
        method is called only once per object. Hence, there should
        be only one object in the list for every object. Otherwise 
        the list is shared with some other object (two objects calls
        append for the same list)"""
        self.my_list.append(self)

    def step_bros_exists(self) -> bool:
        """To all instances only one element has appended to my_list. 
        However if there are more elements in that list, it means that
        this instance is sharing the list with another object."""
        if len(self.my_list) > 1:
            return True
        return False

    @property
    def get_step_bros(self) -> List:
        """Getter for my_self attribute"""
        print("Me and my step brothers:", self.my_list)
        return self.my_list

    @property
    def get_my_list_id(self) -> int:
        "Returns my_list id"
        return id(self.my_list)


def main() -> None:
    """object creation and testing is done in this function"""
    all_objects = []
    all_list_ids = []

    def create_object(number: int) -> None:
        """this methor creates number of MyClass objects, and adds
        them to all_objects list"""
        failed = False
        for i in range(0, number):
            name = "obj_" + str(i)
            obj = MyClass(name)
            all_objects.append(obj)
            list_id = obj.get_my_list_id
            if list_id in all_list_ids:
                print("FAIL: someone else has the same list ID already!",
                      list_id)
                failed = True
            all_list_ids.append(list_id)
        if not failed:
            print(f"- OK! Not a single object has same id(my_list)."
                  f"They are not pointing to the same variable")

    def append_one_item_to_list() -> None:
        """Every object should add themselfs it to their my_list.
        The expected result is that every object has only one item
        in their my_list. Otherwise they are sharing the same list"""
        failed = False
        for obj in all_objects:
            obj.add_item_to_list()
            if obj.step_bros_exists():
                obj.get_step_bros
                failed = True
                print("- FAIL!!! There are more than one item in the my_list",
                      obj.get_step_bros)
        if not failed:
            print(
                f"- OK! Not a single object has more than one item in his my_str. "
                f"In other words, objects are not referring to each others variables."
            )

    def test() -> None:
        """ Lets check if:
        A. are all the my_list id's unique. In other words every id is in the list only once
        B. any of the object has more than one item in their my_list"""
        # TEST A
        failed_a = False

        tmp_id = all_list_ids.copy(
        )  # we want to save the original list for debug
        while len(tmp_id) > 0:
            id = tmp_id.pop()  #Let's take the last element and remove it
            #print("", id, end='')
            if id in tmp_id:
                print(
                    "\n- FAIL!!! \tThere indeed has shared lists!!! id(my_list) = ",
                    id)
                failed_a = True
        if not failed_a:
            print(f"- OK! all the my_str id's are unique")

        # TEST B
        failed_b = False
        for obj in all_objects:
            if obj.step_bros_exists():
                print("- FAIL!!! These objects are sharing my_list:",
                      obj.get_step_bros())
                failed_b = True
        if not failed_b:
            print("- OK! All the objects has only one item in their list")

    # The actual object creation and testing starts from here:

    create_object(10000)
    append_one_item_to_list()
    test()


if __name__ == "__main__":
    main()
