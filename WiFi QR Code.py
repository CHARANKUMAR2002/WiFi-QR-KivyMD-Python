from kivymd.app import MDApp
from kivy.lang.builder import Builder
from wifi_qrcode_generator import wifi_code
import qrcode
from kivymd.toast import toast
from PIL import Image



class WiFi_QR(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("WiFi QR.kv")

    def generate(self):
        name = self.root.ids.name.text
        pro = self.root.ids.auth_type.text
        protection = pro.upper()
        password = self.root.ids.password.text
        if len(name) == 0:
            toast(text="Fill The Fields!", duration=1.5)
        else:
            if len(protection) == 0:
                wifi = wifi_code(ssid=name, hidden=False, authentication_type=protection, password=None)
                qr = qrcode.make(wifi)
                with open(f"{name}.png", 'wb') as f:
                    qr.save(f)
                toast("QR Code Generated!", duration=1.5)
                self.root.ids.image.icon = f"D:\KivyMD\KivyMD\QR Code WiFi\{name}.png"
            else:
                wifi = wifi_code(ssid=name, hidden=False, authentication_type=protection, password=password)
                qr = qrcode.make(wifi)
                with open(f"{name}.png", 'wb') as f:
                    qr.save(f)
                toast("QR Code Generated", duration=1.5)
                self.root.ids.image.icon = f"{name}.png"
    def clear(self):
        self.root.ids.name.text = ""
        self.root.ids.auth_type.text = ""
        self.root.ids.password.text = ""
        self.root.ids.image.icon = f"img.png"
        toast("Cleared Fields!", duration=1)
    def profile(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            toast("Dark Mode On", duration=1)
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.accent_palette = "Red"
        else:
            self.theme_cls.theme_style = "Light"
            toast("Dark Mode Off", duration=1)
            self.theme_cls.primary_palette = "Green"
    def show(self):
        name = self.root.ids.name.text
        img =self.root.ids.image.icon
        if img == "img.png":
            toast("Create A QR Code First!")
        else:
            qr = Image.open(f"{name}.png")
            qr.show()

WiFi_QR().run()