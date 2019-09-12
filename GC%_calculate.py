sequentie =""

aantal_a = sequentie.count("A")
aantal_c = sequentie.count("C")
aantal_g = sequentie.count("G")
aantal_t = sequentie.count("T")
lengte = (sequentie.count("A") + sequentie.count("C") +
sequentie.count("G") + sequentie.count("T"))

gc_percent = (aantal_g + aantal_c) / lengte * 100

print("GC%:", gc_percent)
