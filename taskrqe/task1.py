def roots_quadratic_equation(a, b, c):
    if a == 0:
        raise Exception('Значение "a" не должно быть 0')

    result = []
    condition = b**2 - 4*a*c
    if condition < 0:
        result.append(None)
        result.append(None)
        return result

    if condition == 0:
        result.append(-b/(2 * a))
        result.append(None)
    else:
        result.append((-b - (condition)**0.5) / (2 * a))
        result.append((-b + (condition)**0.5) / (2 * a))

    return result


if __name__ == "__main__":
    a = 1
    b = 2
    c = 50

    result = roots_quadratic_equation(a, b, c)
    print(result)
