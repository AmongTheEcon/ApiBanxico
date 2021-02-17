import urllib.request, urllib.parse, urllib.error
import json
import ssl

mi_token = '5e994f9a97bd4db9a563c2c30edd0d5418f4a913c6d1f7b28b65f349e2c4dac4'
serviceurl = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'
idserie = input('Escriba el idSerie que desea consultar (max 20, separe con comas, sin espacios)')
series_a_consultar = idserie.split(',')
x = len(series_a_consultar)
print('Series a consultar', series_a_consultar, 'Número de series a consultar', x)
series = dict()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for serie in series_a_consultar :
#SACAREMOS LOS METADATOS
    url = serviceurl + serie + '?' + 'token=' + mi_token
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved data URL', url, len(data), 'characters')
    metadatos = json.loads(data)
#VAMOS A AGREGAR EL DICCIONARIO DE DATOS EN EL DICCIONARIO PRINCIPAL DE METADATOS JSON
    url_datos = serviceurl + serie + '/' + 'datos/' + '2000-01-01/2020-12-01' + '?' + 'incremento=PorcObsAnt' + '&token=' + mi_token
    uh_datos = urllib.request.urlopen(url_datos, context=ctx)
    data_datos = uh_datos.read().decode()
    #print('Retrieved data URL', url_datos, len(data_datos), 'characters')
    datos_serie = json.loads(data_datos)
#AGREGAR LOS DATOS A LOS METADATOS Y ESTO AL DICCIONARIO DE SERIES
    datos = datos_serie['bmx']['series'][0]['datos']
    metadatos['bmx']['series'][0]['datos'] = datos
    series[serie] = metadatos['bmx']['series']
    print('len de los datos', len(datos))
#print(json.dumps(series, indent=4))
print(series.keys())
#SE HARÁ LA VISUALIZACIÓN CON JAVASCRIPT Y D3.JS
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
    for serie in series:
        #for observacion in range(len(series[serie][0]['datos'])) :
        val = series[serie][0]['datos'][observacion]['dato']
        fhand.write(","+str(val))
    fhand.write("]");
fhand.write("\n];\n")
fhand.close()
