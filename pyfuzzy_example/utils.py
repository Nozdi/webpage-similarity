
def change_unicode_to_str(system):
    for key, val in system.variables.items():
        for akey in val.adjectives:
            val.adjectives[str(akey)] = val.adjectives.pop(akey)
