def hex_to_rgb(hex):
    h = hex.group()[1:]
    out=[]
    if len(h)<6:
        h = "".join([c*2 for c in h])
    b=bytes.fromhex(h)
    for i in b:
        out.append(i)
    if len(out) > 3:
        s = out.pop()
        return(f'rgba({" ".join(str(d) for d in out)} / {round(s / 255, 5)})')
    return f'rgb({" ".join(str(d) for d in out)})'

if __name__ == "__main__":
    import re
    cases = (('simple.css', 'simple_expected.css'),
        ('advanced.css','advanced_expected.css'))

    for case in cases:
        with open(case[0], 'r') as problem, open(case[1], 'r') as expected:
            assert re.sub(r'\#[0-9a-fA-F]+', hex_to_rgb, problem.read()) == expected.read()