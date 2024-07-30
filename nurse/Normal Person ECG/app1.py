from flask import Flask, render_template, request, send_from_directory, send_file
import os
import test2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upllo.html')

@app.route('/copyfile', methods=['POST'])
def copy_file():
    file = request.files['file']
    folder_path = 'tesing_image'
    file.save(os.path.join(folder_path, file.filename))
    return 'File copied successfully.'

@app.route('/nur2')
def nur2_page():
    test2.main()
    return render_template('nur2.html')

@app.route('/view_report')

def view_report():
    file_path = 'data/result.txt'
    a = send_file(file_path)
    return a
    # with open(file_path, 'r') as file:
    #     content = file.read()
    # return content

if __name__ == '__main__':
    app.run(port=5001)
    
