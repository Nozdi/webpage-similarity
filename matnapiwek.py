#!/usr/bin/env python
from fuzzy.storage.fcl.Reader import Reader
from fuzzy.doc.plot.matplotlib.doc import Doc  # less errors :)


def main():
    system = Reader().load_from_file("napiwek.fcl")

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
    d.createDocSets(
        {"accumulated": system.variables["napiwek"].defuzzify.accumulated_set},
        "accumulated set"
    )
    d.createDocSets(system.variables["napiwek"].defuzzify.activated_sets, "activated sets")

    #other possibilitis:
    import matplotlib.pyplot as plt
    plt.figure(6)
    d.build2DPlot(plt.gca(), system, "obsluga", "napiwek")

    plt.figure(7)
    d.build3DPlot(plt.gca(projection="3d"), system, 'obsluga', 'jedzenie', 'napiwek',
                  input_dict={name: 0.0 for name in system.variables.keys()})

    plt.show()


if __name__ == '__main__':
    main()
