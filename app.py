from flask import Flask, request, render_template
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_img = None

    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            qr_code_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('index.html', qr_code_img=qr_code_img)

if __name__ == '__main__':
    app.run(debug=True)
