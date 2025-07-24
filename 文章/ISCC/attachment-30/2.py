from PIL import Image
 
def xor_images(img1_path, img2_path, output_path):
    # 打开图片
    img1 = Image.open("flag.png")
    img2 = Image.open("flag_is_not_here.jpg")
    
    # 确保两张图片的尺寸相同
    if img1.size != img2.size:
        raise ValueError("两张图片的尺寸必须相同！")
    
    # 将图片转换为单色模式（1位深度）
    img1 = img1.convert('1')
    img2 = img2.convert('1')
    
    # 获取像素数据
    pixels1 = img1.getdata()
    pixels2 = img2.getdata()
    
    # 创建新的像素数据
    xor_pixels = []
    for p1, p2 in zip(pixels1, pixels2):
        # 将255转为1，0转为0
        val1 = 1 if p1 == 255 else 0
        val2 = 1 if p2 == 255 else 0
        
        # 进行异或运算
        xor = val1 ^ val2
        
        # 将结果转回255或0
        new_pixel = 255 if xor else 0
        xor_pixels.append(new_pixel)
    
    # 创建新的图片
    output_img = Image.new('1', img1.size)
    output_img.putdata(xor_pixels)
    
    # 保存结果
    output_img.save(output_path)
 
# 使用示例
img1_path = 'flag.png'  # 替换为你的 PNG 图片路径
img2_path = 'flag_is_not_here.jpg'  # 替换为你的 JPG 图片路径
output_path = 'final_flag.png'#输出flag二维码的名字
 
xor_images(img1_path, img2_path, output_path)