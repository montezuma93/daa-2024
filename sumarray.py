
def sum_of_element(a, b, c, d, e):
    number_array = [a, b, c, d, e]
    total_sum = 0

    #for element in number_array:
     #   total_sum = total_sum + element

    for index in range(len(number_array)):
        print("index: " + str(index) + "value" + str(number_array[index]))
        total_sum = total_sum + number_array[index]


    print(total_sum)

if __name__ == "__main__":
    sum_of_element(5,3,6,2,1)




