for num_beers in range(99, 0, -1):
   if num_beers > 1:
      print num_beers, "bottles of beer on the wall,", num_beers, "bottles of beer."
      if num_beers > 2:
         vers = str(num_beers - 1) + " bottles of beer on the wall."
      else:
         vers = "1 bottle of beer on the wall."
   elif num_beers == 1:
      print "1 bottle of beer on the wall, 1 bottle of beer."
      vers = "no more beer on the wall!"
   print "if one of those bottles should happen to fall,", vers
