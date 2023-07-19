numbers = [1, 2, 3]
age = 100

def grand_parent_func():
    def parent_func():
        global age
        age = 30
        numbers[2] = 1000
        def child_func():
            age = 20
            print(age, 'child_func')

        child_func()
        print(age, 'parent_func')

grand_parent_func()
print(age, 'global')

print(numbers)