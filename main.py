from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PIXABAY_API_KEY = '33648314-a0c30bb8b8f2e270a8ad44f2d' #visivel para estudos


@app.route('/')
def index():
    # Obtém a consulta do usuário a partir dos parâmetros GET na URL
    query = request.args.get('query', default='cat', type=str)

    # Faz uma solicitação HTTP para a API do Pixabay para obter imagens com base na consulta
    response = requests.get(f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo')

    # Analisa o JSON da resposta da API para obter os URLs das imagens
    data = response.json()
    image_urls = [result['webformatURL'] for result in data['hits']]

    # Renderiza um modelo HTML que exibe as imagens em uma galeria
    return render_template('index.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run(debug=True)
