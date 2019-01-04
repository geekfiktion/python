countries = {'AF': 'Afghanistan', 'AL': 'Albania', 'DZ': 'Algeria'}

for (code, country) in countries.items():
    print('<option value="{0}">{1}</option'.format(code, country))
