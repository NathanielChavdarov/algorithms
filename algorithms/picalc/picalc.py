def picalc(num_of_iterations: int) -> float:
    counter = 0
    x_input = 0
    p_squared = num_of_iterations * num_of_iterations
    while x_input <= num_of_iterations:  #
        y_input = 0
        x_squared = x_input * x_input
        while y_input <= num_of_iterations:
            y_squared = y_input * y_input
            sum_xy_squared = x_squared + y_squared
            if sum_xy_squared <= p_squared:
                counter += 1
            y_input += 1
        x_input += 1
    result = counter * 4 / p_squared
    return result
