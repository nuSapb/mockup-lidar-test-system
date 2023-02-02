import numpy as np

def test_laser_component():
    # Generate mock measurement data using numpy's random functions
    laser_output_power = np.random.normal(loc=50, scale=5, size=100)
    laser_stability = np.random.normal(loc=0.1, scale=0.01, size=100)
    laser_beam_shape = np.random.normal(loc=1, scale=0.1, size=100)
    laser_divergence = np.random.normal(loc=0.01, scale=0.001, size=100)
    
    # Verify laser output power
    if np.mean(laser_output_power) < 45 or np.mean(laser_output_power) > 55:
        print("Laser output power test failed")
    else:
        print("Laser output power test passed")
    
    # Test laser stability
    if np.mean(laser_stability) > 0.15 or np.mean(laser_stability) < 0.05:
        print("Laser stability test failed")
    else:
        print("Laser stability test passed")
    
    # Test laser beam shape and divergence
    if np.mean(laser_beam_shape) > 1.5 or np.mean(laser_beam_shape) < 0.5:
        print("Laser beam shape test failed")
    else:
        print("Laser beam shape test passed")
        
    if np.mean(laser_divergence) > 0.015 or np.mean(laser_divergence) < 0.005:
        print("Laser divergence test failed")
    else:
        print("Laser divergence test passed")

# Call the test function
test_laser_component()
