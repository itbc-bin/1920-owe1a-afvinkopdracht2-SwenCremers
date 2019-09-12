sequentie =""

aantal_a = sequentie.count("A")
aantal_c = sequentie.count("C")
aantal_g = sequentie.count("G")
aantal_t = sequentie.count("T")
lengte = (sequentie.count("A") + sequentie.count("C") +
sequentie.count("G") + sequentie.count("T"))

print("lengte:", lengte,"\n" "A:", aantal_a,"\n" "C:", aantal_c, "\n" "G:",
      aantal_g, "\n" "T:", aantal_t)
