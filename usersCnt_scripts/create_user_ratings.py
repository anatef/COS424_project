import fileinput

userId = "1"
counter = 0
print "userId,ratingsCount"
for line in fileinput.input("ratings.csv"):
  if line.find("Id")>=0:
    continue
  lineUserId = line.split(",")[0]
  if userId != lineUserId:
    print userId + "," + str(counter)
    userId = lineUserId
    counter = 0
  counter+=1