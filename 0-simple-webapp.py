import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of course reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs reppresent course review analysis')
    return wp

jp.justpy(app)