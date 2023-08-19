def calcular_combustible(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError

        percentage = (x / y) * 100

        if percentage < 1:
            return 'E'
        elif percentage > 99:
            return 'F'
        else:
            return f'{round(percentage)}%'

    except ZeroDivisionError:
        return "Error: El denominador no puede ser cero."
    
