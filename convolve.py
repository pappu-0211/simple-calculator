from PIL import image,ImageEnhance
import matplotlib.pyplot as plt
img=image.open("dog.jpg")
mods=[("original",img),("brightness",imageEnhance.brightness(img).enhance(1.5)),
      ("contrast",imageEnhance.contrast(img).enhance(1.5)),
      ("sharpness",imageEnhance.sharpness(img).enhance(2.0)),
      ("color",imageEnhance.color(img).enhance(1.8))]
plt.figure(figsize=(15,8))
for i,(t,im)in enumerate(mods):
    plt.subplot(2,3,i+1)
    plt.imshow(im)
    plt.title(t)
    plt.axis("off")
plt.tight_layout()
plt.show()