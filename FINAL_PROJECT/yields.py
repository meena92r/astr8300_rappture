import Rappture
import sys
import wnutils.xml as wx



def main():
    xml = wx.Xml('ww.xml')

    property = 'initial mass'
    io = Rappture.library(sys.argv[1])

    species = io.get('input.string(sp).current')
    z = float(io.get('input.number(Z).current'))

#    zone_xpath = '[@label3 = ' + z + ']'
#    zone_xpath = z #'[@label3 = 0.01]'
#     print zone_xpath,str(z)

    zone_xpath = '[@label3 = ' + str(z) + ']'
    mass_fractions = xml.get_mass_fractions([species], zone_xpath = zone_xpath)
    x = mass_fractions[species]

    props = xml.get_properties_as_floats([property], zone_xpath = zone_xpath)
    mass = props[property]

    # Sort lists by stellar mass

    mass, x = zip(*sorted(zip(mass, x)))

    io.put('output.curve(result0).about.label','z',append=0)
    io.put('output.curve(result0).yaxis.label','X')
    io.put('output.curve(result0).xaxis.label','M')
    

    for i in range(len(mass)):
        io.put(
                'output.curve(result0).component.xy',
                '%g %g\n' % (mass[i],x[i]), append=1
              )    
    
    Rappture.result(io)
    
    
if __name__ == "__main__":
    main()
