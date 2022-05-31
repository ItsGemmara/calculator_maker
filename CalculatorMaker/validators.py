class RawFormulaValidators:

    def division_validators(self, raw_formula):
        index = -1
        for i in raw_formula:
            index += 1
            if index < (len(raw_formula) - 1):
                next_elm = raw_formula[index + 1]
            else:
                next_elm = None
            pre_elm = raw_formula[index - 1]
            try:
                int(i)
            except:
                if i == '/':
                    if next_elm:
                        try:
                            int(next_elm)
                            int(pre_elm)
                        except:
                            raise ValueError('This error occurs when you try to divide anything other than numbers')
                        if next_elm == '0':
                            raise ZeroDivisionError('ZeroDivisionError occurs when a number is divided by a zero')
        return raw_formula


class FormulaValidators:

    def create_formula(self, pre_formula):

        raw_formula_validators = RawFormulaValidators()
        raw_formula = raw_formula_validators.division_validators(pre_formula)
        formula_list = list()
        numb = ''
        for i in raw_formula:
            try:
                int(i)
                numb += i
            except:
                formula_list.append(int(numb))
                numb = ''
                formula_list.append(i)
        formula_list.append(int(numb))
        return formula_list



