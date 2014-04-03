#!/usr/bin/env python
from fuzzy.storage.fcl.Reader import Reader
from fuzzy.doc.plot.gnuplot.doc import Doc
from utils import change_unicode_to_str


def main():
    system = Reader().load_from_file("napiwek.fcl")
    change_unicode_to_str(system)  # unicode does not work on plots

    d = Doc(".")
    d.createDoc(system)

    input_variables = {
        "obsluga": 3.,
        "jedzenie": 8.,
    }
    output_variables = {
        "napiwek": None
    }
    system.calculate(input_variables, output_variables)
    print(output_variables)
    d.createDocSets({"accumulated": system.variables["napiwek"].defuzzify.accumulated_set}, "accumulated set")


if __name__ == '__main__':
    main()
