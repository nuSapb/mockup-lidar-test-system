import numpy as np

def optics_component_test():
    # Generate mockup data for lens quality and focus test
    lens_quality = np.random.normal(loc=100, scale=5)

    # Generate mockup data for optical alignment test
    optical_alignment = np.random.normal(loc=0, scale=0.01)

    # Generate mockup data for optical aberrations test
    optical_aberrations = np.random.normal(loc=0, scale=0.001)

    # Return the mockup test data
    return lens_quality, optical_alignment, optical_aberrations

# Call the function to get the mockup data
lens_quality, optical_alignment, optical_aberrations = optics_component_test()

# Print the mockup data
print("Lens quality: ", lens_quality)
print("Optical alignment: ", optical_alignment)
print("Optical aberrations: ", optical_aberrations)
