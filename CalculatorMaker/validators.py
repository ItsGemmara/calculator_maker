
def formula_validators(raw_formula, variables_list):

    index = -1
    for i in raw_formula:
        index += 1
        next_elm = raw_formula[index + 1]
        pre_elm = raw_formula[index - 1]
        try:
            int(i)
        except:
            if i == '/':
                try:
                    int(next_elm)
                    if next_elm == '0':
                        raise ZeroDivisionError('ZeroDivisionError occurs when a number is divided by a zero')
                except:
                    if i not in variables_list:
                        raise ValueError(f'the {next_elm} is not one of the variables or numbers')
            elif i in
    return raw_formula

