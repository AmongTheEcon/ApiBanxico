fhand = open('banxicoline.js','w')
fhand.write("gline = [ ['Fecha'")
for serie in series:
    fhand.write(",'"+series[serie][0]['titulo']+"'")
fhand.write("]")
for observacion in range(len(series[serie][0]['datos'])) :
    fhand.write(",\n['"+series[series_a_consultar[0]][0]['datos'][observacion]['fecha']+"'")
#for observacion in range(len(series[serie][0]['datos'])) :
#    for serie in series :
        #fhand.write(",\n['"+series[serie][0]['datos'][observacion]['fecha']+"'")
    for serie in series :
        #for observacion in range(len(series[serie][0]['datos'])) :
        val = series[serie][0]['datos'][observacion]['dato']
        fhand.write(","+str(val))
    fhand.write("]");
fhand.write("\n];\n")
fhand.close()
