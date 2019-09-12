#reads a flat text file and uses the count and
#len function to calculate the length and GC% and prints these
sequentie = open("DictyosteliumDiscoideumMRNANoEnters.txt")
sequentie = sequentie.read()

aantal_g = sequentie.count("G")
aantal_c = sequentie.count("C")
lengte = len(sequentie)
gc_percent = (aantal_g + aantal_c) / lengte * 100

print("G:", aantal_g, "\n" "C:", aantal_c, "\n"  "lengte:"
      , lengte,"\n"  "GC%:", gc_percent  )
