import sys
import wnutils.xml as wx
import wnutils.base as wb
import matplotlib.pyplot as plt

xml = wx.Xml(sys.argv[1])

species = sys.argv[2]
metallicities = ['0', '1.e-4', '1.e-2', '0.1', '0.5', '1', '2']
property = 'initial mass'

b = wb.Base()
latex = b.get_latex_names([species])

for z in metallicities:

    zone_xpath = '[@label3 = ' + z + ']'
    mass_fractions = xml.get_mass_fractions([species], zone_xpath = zone_xpath)
    x = mass_fractions[species]

    props = xml.get_properties_as_floats([property], zone_xpath = zone_xpath)
    mass = props[property]

    # Sort lists by stellar mass

    mass, x = zip(*sorted(zip(mass, x)))

    plt.plot(mass, x, '-o', label=z)

#plt.yscale('log')

plt.xlim([10,50])

plt.xlabel('${\\rm M}\ ({\\rm M_\odot})$')

plt.ylabel('X(' + latex[species] + ')')

plt.legend(title = '${\\rm Z / Z_\odot}$')

plt.show() 
