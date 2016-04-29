import fileinput

userId = "1"
counter = 0
all_genres = set()
print "userId,ratingsCount"
for line in fileinput.input("movies.csv"):
  if line.find("Id")>=0:
    continue
  lineGenresString = line.split(",")[-1].replace("\n","").replace("\r","")
  lineGenres = set()
  if lineGenresString.find("|") >=0:
     lineGenres = set(lineGenresString.split("|"))
  else:
     lineGenres = set([lineGenresString])
  if "A" in lineGenres:
    print line,lineGenres
  all_genres = all_genres | lineGenres 
print all_genres
