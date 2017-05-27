from elaphe import barcode
barcode('qrcode','Hello Barcode Writer In Pure PostScript.', options=dict(version=9, eclevel='M'), margin=10, data_mode='8bits'))   # Generates PIL.EpsImageFile instance
##<PIL.EpsImagePlugin.EpsImageFile ... at ...>
#> _.show() # Show rendered bitmap