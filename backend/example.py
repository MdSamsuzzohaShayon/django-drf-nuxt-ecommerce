import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "shayon-cloud", 
  api_key = "455739236686664", 
  api_secret = "01IJQKbkaEl4ZMng8xzuSH0AAfs",
  secure = True
)

res = cloudinary.uploader.destroy('ecom/l9ul7sdxfxbjdkoqfege')
print(res)