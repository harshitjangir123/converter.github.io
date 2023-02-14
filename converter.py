# Unit Converter

def convert(temp, from_unit, to_unit):
    # Convert temperature from one unit to another
    if from_unit == "C" and to_unit == "F":
        return (temp * 1.8) + 32
    elif from_unit == "F" and to_unit == "C":
        return (temp - 32) / 1.8
    elif from_unit == "C" and to_unit == "K":
        return temp + 273.15
    elif from_unit == "K" and to_unit == "C":
        return temp - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (temp + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "F":
        return (temp * 9/5) - 459.67
    else:
        return temp

# Test the function with sample inputs
print(convert(100, "C", "F")) # should print 212.0
print(convert(32, "F", "C")) # should print 0.0
print(convert(0, "C", "K")) # should print 273.15
print(convert(273.15, "K", "C")) # should print 0.0
