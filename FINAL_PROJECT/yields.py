import Rappture
import sys
import wnutils.xml as wx



def main():
    xml = wx.Xml('ww.xml')

    properties = ['initial mass', 'total ejected mass']
    io = Rappture.library(sys.argv[1])

    species = io.get('input.string(sp).current')
    z = io.get('input.number(Z).current')

    zone_xpath = '[@label3 = ' + str(z) + ']'
    mass_fractions = xml.get_mass_fractions([species], zone_xpath = zone_xpath)

    x = mass_fractions[species]

    if len(x) == 0:
        my_str = 'Invalid metallicity'
        io.put('output.string(result0).about.label', 'Diagnostic')
        io.put('output.string(result0).current', my_str)
        Rappture.result(io)
        exit()

    props = xml.get_properties_as_floats(properties, zone_xpath = zone_xpath)

    mass = props['initial mass']
    ejected_mass = props['total ejected mass']

    # Sort lists by stellar mass

    mass, x, ejected_mass = zip(*sorted(zip(mass, x, ejected_mass)))

    label_str0 = 'Yields for ' + species
    label_str1 = 'Ejected mass (in solar masses) of ' + species

    io.put('output.curve(result0).about.label', label_str0,append=0)
    io.put('output.curve(result0).xaxis.label','Stellar Mass (solar masses)')
    io.put('output.curve(result0).yaxis.label', 'Mass Fraction')
    
    io.put('output.curve(result1).about.label', label_str1,append=0)
    io.put('output.curve(result1).xaxis.label','Stellar Mass (solar masses)')
    io.put('output.curve(result1).yaxis.label', 'Ejected Mass')
    

    for i in range(len(mass)):
        io.put(
                'output.curve(result0).component.xy',
                '%g %g\n' % (mass[i],x[i]), append=1
              )    
        io.put(
                'output.curve(result1).component.xy',
                '%g %g\n' % (mass[i],x[i] * ejected_mass[i]), append=1
              )    
    
    io.put('output.string(result2).about.label', 'Diagnostic', append=0)
    io.put('output.string(result2).current', 'Metallicity found')

    Rappture.result(io)
    
    
if __name__ == "__main__":
    main()
