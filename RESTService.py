from flask import Flask, request
import json
import base64
from PIL import Image
from io import BytesIO
import subprocess
from orbpro import retornaImagenes
from flask_cors import CORS, cross_origin

#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def convertirListaImagensAJson(parLista):
    
    {'topImagenes': {}}
    strRes = '['
    for element in parLista:
        obj = {}
        print(element)
        obj = {'nombreImagen': element}
        json_string = json.dumps(obj)
        strRes += json_string
        strRes += ','
    strRes = strRes[:-1]
    strRes += ']'
    return strRes

def crearRespuesta(lista1):

    strTopImagenes = convertirListaImagensAJson(lista1)
    print('Finali')      
    objRes = {'topImagenes': json.loads(strTopImagenes)}
    strRes = json.dumps(objRes)
    return objRes;
    
@app.route('/buscarImagen', methods=['POST'])
def pruebaPost():
    print('Comenzando proceso de recuperación de imagenes...');
    req_data = request.get_json()
    strImg = req_data['base64img'] 
 
    strImg = strImg.replace('data:image/jpeg;base64,','')
    im = Image.open(BytesIO(base64.b64decode(strImg)))
    im.save('imagenRecibida.jpg', 'JPEG')
    imageSele=retornaImagenes()
   
    result = crearRespuesta(imageSele) 
    print('Finalizada recuperación de imagenes. Enviando resultados. ')
        
    return result


if __name__ == '__main__':
     app.run(port='8080')
