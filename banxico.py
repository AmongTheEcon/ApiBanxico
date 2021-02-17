import urllib.request, urllib.parse, urllib.error
import json
import ssl

mi_token = '5e994f9a97bd4db9a563c2c30edd0d5418f4a913c6d1f7b28b65f349e2c4dac4'
serviceurl = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'
idserie = input('Escriba el idSerie que desea consultar (max 20, separe con comas, sin espacios)')
series_a_consultar = idserie.split(',')
print('Series a consultar', series_a_consultar)
x = len(series_a_consultar)
print('Número de series a consultar', x)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#SACAREMOS LOS METADATOS
url = serviceurl + idserie[:] + '?' + 'token=' + mi_token
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved data URL', len(data), 'characters')
metadatos = json.loads(data)
#VAMOS A AGREGAR EL DICCIONARIO DE DATOS EN EL DICCIONARIO PRINCIPAL DE METADATOS JSON
url_datos = serviceurl + idserie[:] + '/datos' + '?' + 'token=' + mi_token
print('Retrieving', url_datos)
uh_datos = urllib.request.urlopen(url_datos, context=ctx)
data_datos = uh_datos.read().decode()
print('Retrieved data URL', len(data_datos), 'characters')
datos_serie = json.loads(data_datos)
for serie_consultada in range(x) :
    print(serie_consultada)
    datos = datos_serie['bmx']['series'][serie_consultada]['datos']
    metadatos['bmx']['series'][serie_consultada]['datos'] = datos
print(json.dumps(metadatos, indent=4))
