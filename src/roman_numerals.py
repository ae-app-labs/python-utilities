def convert_to_roman(year):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ""
    for value, numeral in roman_numerals.items():
        while year >= value:
            result += numeral
            year -= value
    return result

year_to_convert = int( input("Enter the year: "))
roman_numeral = convert_to_roman(year_to_convert)

print(f"The Roman numeal for {year_to_convert} is: {roman_numeral}")
