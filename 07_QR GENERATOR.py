import qrcode

class MyQR(object):
    def __init__(self, data:str, size:int, padding:int, file_name:str):
        self.data = data
        self.size = size
        self.padding = padding
        self.file_name = file_name
        
    def make_qr(self):
        qr = qrcode.QRCode(box_size = self.size, border = self.padding)
        qr.add_data(self.data)
        img = qr.make_image(back_color = "white", fill_color="black")
        img.save(f"{self.file_name}.png")
        
if __name__ == "__main__":
    data = "This is me."
    myqr = MyQR(data, 100, 5, 'qr')
    myqr.make_qr()
        
        
        
