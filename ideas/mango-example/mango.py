import dryscrape

dryscrape.start_xvfb()

sess = dryscrape.Session(base_url = 'http://shop.mango.com')
sess.set_attribute('auto_load_images',False)
sess.visit('/ES/m/hombre/prendas/todas/?m=coleccion')

print sess.at_xpath("//*[@class=\"searchResultPrice\"]").text()
