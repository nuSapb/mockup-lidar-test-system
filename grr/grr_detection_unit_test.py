import numpy as np

def detection_unit_test():
    # Generate a random test measurement data for detection unit using numpy
    detection_sensitivity = np.random.uniform(85, 95)
    detection_range = np.random.uniform(50, 100)

    # Define the test criteria
    detection_sensitivity_min = 85
    detection_sensitivity_max = 95
    detection_range_min = 50
    detection_range_max = 100

    # Evaluate the test result
    result = True
    if detection_sensitivity < detection_sensitivity_min or detection_sensitivity > detection_sensitivity_max:
        result = False
    if detection_range < detection_range_min or detection_range > detection_range_max:
        result = False
    
    return result

def grr_detection_unit_test(n=10):
    # Repeat the detection unit test n times
    results = []
    for i in range(n):
        results.append(detection_unit_test())
    
    # Calculate the GR&R using numpy
    grr = np.sum(results) / n
    
    # Return the GR&R result
    return grr

# Call the GR&R function to perform GR&R of the detection unit test
grr_result = grr_detection_unit_test()
print("GR&R result of the detection unit test:", grr_result)
