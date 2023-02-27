years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233,
          697_852, 696_271, 679_106, 657_076, 640_370]


def annual_births_average(year=years, births=births):
    '''Return a list of tuples with each entry in this format
       (year, birth, running_average)
       Round the running_average to the nearest integer. 
    '''
    result = list()
    acc_births = int()
    for idx, (year, birth_per_year) in enumerate(zip(years, births), start=1):
        acc_births += birth_per_year
        result.append((year, birth_per_year, round(acc_births/(idx))))
    return result
