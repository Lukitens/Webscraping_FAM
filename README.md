# Web scraping:

Para este código de web scraping use Scrapy para poder extraer datos de todos los atletas de la federación atlética metropolitana.
El código se ejecuta poniendo lo siguiente en la terminal:
scrapy runspider webscrap.py -o atletas.json -t json -s FEED_EXPORT_ENCODING=utf-8

A la hora de ejecutar el código es importante estar en la misma carpeta en la que se encuentra el archivo .py
