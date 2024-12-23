from flask import Flask, render_template

# สร้าง instance ของ Flask
app = Flask(__name__)

# Route แรก (หน้าแรก)
@app.route('/')
def home():
    return render_template('index.html')  # ส่งไฟล์ HTML กลับไปแสดงผลที่ client

# Route สำหรับ content.html
@app.route('/next-content-section')
def content():
    return render_template('content.html')

# ตรวจสอบให้โปรแกรมรันเมื่อไฟล์ถูกเรียกใช้งานโดยตรง
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)