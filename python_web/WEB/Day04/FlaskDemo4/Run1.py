import os

from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
    # 根据用户的请求意图去执行不同的功能
    if request.method == 'GET':
        return render_template('01-upload.html')
    else:
        uname = request.form['uname']
        print("用户名称"+uname)
        f = request.files['uimg']
        # 获取时间字符串
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        # 获取文件的后缀名
        ext = f.filename.split('.')[1]
        # 拼文件名
        filename = ftime+'.'+ext
        print('图片名称:'+filename)
        # 拼目录
        basedir = os.path.dirname(__file__)
        upload_path = os.path.join(basedir,'static/upload',filename)
        print('upload_path:'+upload_path)
        f.save(upload_path)
        return "Upload Success"

if __name__ == "__main__":
    app.run(debug=True)