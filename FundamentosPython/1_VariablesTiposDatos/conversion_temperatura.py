c = 45 #g celsius
f = 80 #g fahrenheit

def celsius_a_fahrenheit(celsius):
    return(celsius* 9/5) +32

def fahrenheir_a_celsius(fahrenheit):
    return(fahrenheit - 32) *5/9

f_convertido = celsius_a_fahrenheit(c)
c_convertido = fahrenheir_a_celsius(f)

print(f"{c}ºC equivalente a {f_convertido:.2f}ºf")
print(f"{f}ºf equivalente a {c_convertido: .2f}ºc")