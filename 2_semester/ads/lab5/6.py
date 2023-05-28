def exponential_filter(input_data, alpha):
    output_data = [input_data[0]]
    for i in range(1, len(input_data)):
        output_data.append(
            alpha * input_data[i] + (1 - alpha) * output_data[i-1])
    return output_data


print(exponential_filter([1, 2, 3, 4, 5], 0.5))
