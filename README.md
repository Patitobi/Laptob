<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"/>
    <title>Nav_pweb</title>
    <link href="CSS/style.css" rel="stylesheet" type="text/css">
</head>
<body>  
    <header>
        <a href="#" class="logo">LOGO</a>
            <div class="menu-toggle"></div>
            <nav>
                <ul>
                    <li><a href="#" class="active">Home</a></li>
                    <li><a href="#">About Me</a></li>
                    <li><a href="#">Qualifications</a></li>
                    <li><a href="#">My Content</a></li>
                    <li><a href="#">Contact Me</a></li>
                </ul>
            </nav>
		<div class="clearfix"></div>
    </header>
    <main>
        <section id="sec1">
            <a id="title">
                Wilkommen, <br> auf meiner Seite
            </a>
        </section>
        <section id="sec2">
            <a>
                World
            </a>
        </section>
        <section id="sec3">
            <a>
                Moin
            </a>
        </section>
    </main>
    <script
        src="https://code.jquery.com/jquery-3.6.0.js"
        integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
        crossorigin="anonymous">
    </script>
        <script type="text/javascript">
            $(document).ready(function(){
                $('.menu-toggle').click(function(){
                    $('.menu-toggle').toggleClass('active')
                    $('nav').toggleClass('active')
                })
            })
        </script>
</body>
</html>
