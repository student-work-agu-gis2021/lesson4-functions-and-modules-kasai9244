def fahr_to_celsius(temp_fahrenheit):
  """A function that converts temperature from Fahrenheit to Celsius
  Parameters:
  ---------
  temp_fahrenheit:
  float　Fahrenheit temperature
  
  returns:
  ---------
  float celsius temperature
  """

  return (temp_fahrenheit-32) / 1.8

def temp_classifier(temp_celsius):
  if temp_celsius < -2:
    return 0
  elif temp_celsius < 2:
    return 1
  elif temp_celsius < 15:
    return 2
  else:
    return 3
"""A function that classifies temperatures in degrees Celsius by temperature

    Parameter:
    ----------
    temp_celsius : float
        celsius temperature

    returns :
    ----------
    int
        class number
    """
