#importing the modules
import os
from yattag import  Doc
from yattag import  indent



doc, tag, text = Doc().tagtext()

#site header
def site_header():
    with tag('nav',klass="navbar navbar-inverse navbar-fixed-top"):
        with tag('div',klass="container-fluid"):
            with tag('a',klass="navbar-brand", href="#"):
                text("Site Logo")
            with tag('ul',klass="nav navbar-nav navbar-right"):
                increment=1
                for increment in range(4):
                    with tag('li'):
                        with tag('a',href="#"):
                            text("Link ",increment+1)




#jumbotron content
def jumbotron_content():
    with tag('div',klass="jumbotron"):
        with tag('div',klass="container"):
            with tag('h1'):
                text('Welcome to Ehealth Academy')
            texte='''This is a bootstrap Template. It includes a navbar with links and a large jumbotron element. Use it as a starting point to create something more unique.'''
            with tag('p'):
                text(texte)
            with tag('p'):
                with tag('a', klass="btn btn-lg btn-success",role="button",href="#"):
                    text('Join us')






doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Web site Template')
        doc.stag('link',rel="stylesheet",href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css")
        doc.stag('link',rel="stylesheet",href="/css/style.css")
    with tag('body'):
        #called the header and jumbotron function
        site_header()
        jumbotron_content()

        with tag('script', type="text/javascript",src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"):
            text('')
        with tag('script', type="text/javascript",src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"):
            text('')
result = indent(doc.getvalue())
print result


#creating css directory and css file
os.makedirs(os.getcwd()+"\myProject\css")
os.chdir(os.getcwd()+"\myProject\css")
custom_css=open('style.css','wb')
#go back in myProject folder
os.chdir('..')

#creating js directoryand js file
os.makedirs(os.getcwd()+"\js")
os.chdir(os.getcwd()+"\js")
custom_js=open('main.css','wb')
#go back in myProject folder
os.chdir('..')



#creating the index.html file
index = open('index.html','wb')

#addead the content in the index.html file and close it
index.write(result)

index.close()
