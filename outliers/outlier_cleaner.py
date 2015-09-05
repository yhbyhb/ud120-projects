#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    error_dict = {}
    for i in range(0, len(ages)):
        error = abs(predictions[i][0] - net_worths[i][0])
        error_dict[i] = error

    import operator
    sorted_error = sorted(error_dict.items(), key=operator.itemgetter(1))

    for i in range(0, int(round(len(ages) * 0.9))):
        index = sorted_error[i][0]
        cleaned_item = (ages[index][0], net_worths[index][0], sorted_error[i][1])
        cleaned_data.append(cleaned_item)

    return cleaned_data

