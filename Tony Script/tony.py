import os


print("""
<!DOCTYPE html>
<html>
<head>

     <title>Tony</title>
    
     <h1>
        <img class='tony' src='https://img.icons8.com/doodle/480/000000/iron-man.png'/>
        <img class="tony_" src='https://raw.githubusercontent.com/chinathanna001/College/main/logo/tony.png'>
    </h1>

    <link rel="icon" type="image/x-icon" href="https://raw.githubusercontent.com/chinathanna001/College/main/logo/iron-man.png">
    
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9851237424755952"
    crossorigin="anonymous"></script>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    <meta name="Author" content="chinathanna001">

    <meta name="GENERATOR" content="cr VERSION 1.0 created by Sharon Joseph">

</head>

<body>

    <hr>
    <h2 class="he">Data Science Programs<h2>
        <hr>
""")
b='tony.py'
c='tony.cmd'
d='.gitattributes'
e='.git'
f='index.html'
g='.gitignore'

for x in os.listdir():
    y=x.replace(" ","%20")
    if (x==b)|(x==c)|(x==d)|(x==e)|(x==f)|(x==g):
        continue
    else:
        if x.endswith(".pdf"):
            print("<img src='https://img.icons8.com/color/480/000000/pdf.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".txt"):
            print("<img src='https://img.icons8.com/external-fauzidea-flat-fauzidea/480/000000/external-txt-file-file-extension-fauzidea-flat-fauzidea.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".java"):
            print("<img src='https://img.icons8.com/color/480/000000/java-coffee-cup-logo--v1.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".py"):
            print("<img src='https://img.icons8.com/color/480/000000/python--v1.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".c"):
            print("<img src='https://img.icons8.com/color/480/000000/c-programming.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".logic"):
            print("<img src='https://github.com/chinathanna001/College/raw/main/logo/logic_.png'/><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".csv"):
            print("<img src='https://img.icons8.com/office/480/000000/csv.png'><a href='./",y,"'>",x,"</a><br>",sep='')
        elif x.endswith(".xlsx"):
            print("<img src='https://img.icons8.com/external-fauzidea-flat-fauzidea/512/000000/external-xlsx-file-file-extension-fauzidea-flat-fauzidea.png'><a href='./",y,"'>",x,"</a><br>",sep='')        
        else:
            print("<img src='https://img.icons8.com/color/480/000000/folder-invoices--v1.png'><a href='./",y,"/index.html'>",x,"</a><br>",sep='')


print(""" <p><br></p>

<hr>
<p class="VERSION">
             This Website Provide Some Study Material.<br>
             Do not misuse above content.<br>
             Copy is better than taking zero.<br>
             None of these pdf above do not belongs to this website.

            </p>

            <hr>

            <p class="info">
                This Website is Generated by Project script
            </p>
    </body>

    </html>

<style>

    BODY { font-family : monospace, sans-serif;  color: black;}
  P { font-family : monospace, sans-serif; color: black; margin:0px; padding: 0px;}
  A:visited { text-decoration : none; margin : 0px; padding : 0px;}
  A:link    { text-decoration : none; margin : 0px; padding : 0px;}
 
  A:active  { margin : 0px; padding : 0px;}
    body
    {
        background-color: black;
    }

    h1
    {
        color: rgb(0, 255, 0);
    }

    a
    {
        font-size: large;
        color: rgb(0, 255, 0);
        line-height: 35px;
        margin-left:8px;
        transition: background-color 0.3s ease;
    }

    a:hover   
    { 
        transition-timing-function: ease-in;
        color: yellow;
        padding : 0px;}

    img
    {
        height: 30px;
        width: 30px;
        vertical-align: text-bottom;
        margin-left: 25px;
        margin-right: 10px;
    }

    .VERSION
    {
        color: rgb(0, 255, 0);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: small;
    }

    .info
    {
        font-size: xx-small;
    }

    p
    {
          color: rgb(0, 255, 0);
          font-size:large;
          font-family: 'Times New Roman', Times, serif;
    }

    .tony
    {
        height: 100px;
        width: 100px;
    }

    .tony_
    {
        height: 100px;
        width: 211px;
        margin-left: 5px;
    }

    .he
    {
        color: rgb(0, 255, 0);
        font-size: larger;
        margin-left: 5px;
    }




     .dob
     {
        color: rgb(0, 255, 0);
     }

</style>


""")
