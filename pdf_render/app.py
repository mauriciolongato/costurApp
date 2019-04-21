from flask import Flask, render_template, make_response, request
import json
import pdfkit

from helpers import jobs, dados_testes, functions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def box_pdf_render_pdfkit():
    if request.method == 'POST':
        json_data = json.loads(request.data)

        # Cria as imagens dos códigos de barra
        body_with_barcode = []
        for row in json_data['body']:
            row['cod_bar_address'] = functions.path2url('static/{}'.format(jobs.create_barcode(row['cod_bar'])))
            # row['cod_bar_address'] = jobs.create_barcode(row['cod_bar'])
            body_with_barcode.append(row)
        json_data_final = {'header': json_data['header'], 'body': body_with_barcode}

        rendered = render_template('caixa.html', data=json_data_final)
        pdf = pdfkit.from_string(rendered, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response

    else:
        data = dados_testes.informacao_caixa()
        rendered = render_template('caixa.html', data=data)
        # return rendered
        pdf = pdfkit.from_string(rendered, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response


@app.route('/teste', methods=['GET'])
def teste():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
