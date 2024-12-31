import tkinter as tk
from PIL import Image, ImageTk

class ImageCropper:
    def __init__(self, master, path):
        self.master = master
        self.image = Image.open(path)
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Khung chứa cho canvas và thanh cuộn
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=1)

        # Tạo canvas với thanh cuộn ngang và dọc
        self.canvas = tk.Canvas(self.frame, bg="white", width=600, height=400)
        self.scroll_x = tk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Thêm ảnh vào canvas
        self.canvas_img_id = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
        self.canvas.config(scrollregion=self.canvas.bbox(self.canvas_img_id))

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        # Lưu tọa độ bắt đầu kéo
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y)

    def on_drag(self, event):
        # Cập nhật hình chữ nhật khi kéo chuột
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))

    def on_release(self, event):
        # In tọa độ cuối cùng của hình chữ nhật
        end_x, end_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        print("Region selected: ({}, {}) to ({}, {})".format(self.start_x, self.start_y, end_x, end_y))

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageCropper(root, 'C:/vs code/H2O2/h202/raw data/data cut/60uM fn/IMG20240507155053.jpg')
    root.mainloop()
