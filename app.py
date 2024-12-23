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
    # ใช้ PORT จากตัวแปรสภาพแวดล้อม หรือค่าเริ่มต้นเป็น 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
