def throw_stop_iteration():
    iterator = iter([])
    next(iterator)
#throw_stop_iteration()

def throw_zero_division():
    result = 1 / 0
#throw_zero_division()

def throw_assertion_error():
    assert False
#throw_assertion_error()

def throw_import_error():
    import lior_loves_python
#throw_import_error()

def throw_key_error():
    my_dict = {"lior": "avraham"}
    print(my_dict["python"])
#throw_key_error()

def throw_syntax_error():
    eval("print('Hello, world!'")
#throw_syntax_error()

def throw_indentation_error():
    def my_function():
    print("hello")
#throw_indentation_error()

def throw_type_error():
    result = "10" + 5
#throw_type_error()



