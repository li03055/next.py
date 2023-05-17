def get_fibo():
    before_num = 0
    current_num = 1
    while True:
        yield before_num
        next_num = current_num + before_num
        before_num = current_num
        current_num = next_num


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))