from website import create_app
import os

UPLOAD_FOLDER = 'website/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app = create_app()
    app.run()