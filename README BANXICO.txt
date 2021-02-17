API BANXICO

El token de consulta es un requisito necesario para poder utilizar el API de series de tiempo. Consta de 64 caracteres alfanuméricos y debe ser enviado cada vez que 
se interactúe con los servicios provistos. El envío se debe realizar a través del header HTTP Bmx-Token o el parámetro token (El header tiene prioridad, si se envía 
el header se toma este valor en caso contrario se toma el valor del parámetro). Por ejemplo:

Header:
Bmx-Token: e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25
Query:
token=e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25

Mi Token de consulta generado: 5e994f9a97bd4db9a563c2c30edd0d5418f4a913c6d1f7b28b65f349e2c4dac4
Límite de consultas
El API del Sistema de Información Económica, establece un conjunto de límites al número de consultas que se puede realizar por token de consulta. 
Estos límites se establecen por ventana de tiempo y por consultas diarias. Existen 2 ventanas de tiempo: de 1 minuto, para consultas de datos oportunos y metadatos 
de las series, y de 5 minutos para consulta de datos históricos.


Tipo de consulta	Ventana de tiempo	Límite diario	Recursos relacionados
Oportuna	Máximo 80 consultas en 1 minuto	40,000 consultas por día	GET series
GET series/:idSerie
GET series/:idSerie/datos/oportuno
Histórica	Máximo 200 consultas en 5 minutos	10,000 consultas por día	GET series/:idSerie/datos
GET series/:idSerie/datos/:fechaIni/:fechaFin
Por ejemplo si se requieren los metadatos de una serie, sólo se pueden realizar 80 consultas dentro de un periodo de un minuto. 
De forma similar aplica para las consultas históricas, si se solicitan todos los datos de un grupo de series, sólo se pueden realizar 200 peticiones 
en una ventana de 5 minutos. También se debe considerar que no se debe superar el límite diario establecido.
