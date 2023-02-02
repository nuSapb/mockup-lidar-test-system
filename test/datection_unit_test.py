import numpy as np

def detection_unit_test():
    # Generate a random test measurement data for detection unit using numpy random
    detection_sensitivity = np.random.uniform(85, 95)
    detection_range = np.random.uniform(50, 100)
    print('detection_sensitivity: {}'.format(detection_sensitivity))
    print('detection_range: {}'.format(detection_range))

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

# Call the function to perform detection unit test
test_result = detection_unit_test()
if test_result:
    print("Detection unit test passed")
else:
    print("Detection unit test failed")
