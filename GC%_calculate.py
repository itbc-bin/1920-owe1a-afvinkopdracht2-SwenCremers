#reads a flat text file and uses the count and
#len function to calculate the length and GC% and prints these

sequentie = open("DictyosteliumDiscoideumMRNANoEnters.txt")# opens a txt file
sequentie = sequentie.read()# reads the opened txt file

aantal_g = sequentie.count("G")# counts number of G's in a string
aantal_c = sequentie.count("C")# counts number of C's in a string
lengte = len(sequentie)# creates an int using the predefined function len()
gc_percent = (aantal_g + aantal_c) / lengte * 100# calculates gc percentage

print("G:", aantal_g, "\n" "C:", aantal_c, "\n"  "lengte:" 
      , lengte,"\n"  "GC%:", gc_percent  )
