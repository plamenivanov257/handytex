"""
Generates some useful .tex files
"""


def generate_rm():
    """
    Generates definitions for rm symbols.
    """
    with open("./rmsymbols.tex", "w") as file:

        print("% Definitions of rm symbols.", file=file)
        print("% These override anything else with the same name!", file=file)

        for i in range(26):
            char = chr(ord('a') + i)
            print(rf"\def\rm{char}{{{{\rm {char}}}}}", file=file)

            char = chr(ord('A') + i)
            print(rf"\def\rm{char}{{{{\rm {char}}}}}", file=file)



if __name__ == "__main__":
    generate_rm()
