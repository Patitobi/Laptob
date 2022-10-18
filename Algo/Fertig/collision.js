// festlegen von größe und sonnstige pflicht sachen
var canvas = document.querySelector('canvas');
var startstop = false;
var c = canvas.getContext('2d');

var gravati = 1;
var friction = 0.9;

canvas.height= Math.round((window.innerHeight/100)*83);
canvas.width=Math.round((window.innerWidth/100)*93);

//kreis objekt
function Kreis(x, y, xm, ym, radius, collor){
    this.x=x;
    this.y=y;
    this.xm = xm;
    this.ym = ym;
    this.radius=radius;
    this.collor=collor;

    //bildet objekt in canvas ab
    this.draw = function(){
        c.beginPath();
        c.arc(this.x, this.y, this.radius, 0, Math.PI*2, false);
        c.strokeStyle=this.collor;
        c.fillStyle=this.collor;
        c.fill();
        c.stroke();
    }
    //checkt für bedingungen jeden durlauf
    this.update = function(can_innerHeight, can_innerWidth){

        //wenn ab boden
        if(this.y+this.radius+this.ym>=can_innerHeight){
            this.ym=-this.ym*friction;
        } else{
            //constane runter bewegung
            this.ym+=gravati;
        }
        //wenn lings oder echts am rand
        if (this.x+this.radius+this.xm>can_innerWidth||this.x-this.radius<0){
            this.xm*=-1;
        }
        
        //neue position
        this.x+=this.xm;
        this.y+=this.ym;

        this.draw();
    }
}

//start und stop knopf
function start_stop(x){
    if(x && !startstop){
        startstop=true;
        init();
    }
    else if(!x && startstop){
        startstop = false;
    }
        animate();
}

function distans(a, b){

    var xdis = a.x- b.x;
    var ydis = a.y - b.y;

    return Math.sqrt(Math.pow(ydis,2)+Math.pow(xdis,2));
}

// erstellen von objekten
var ballArrry;
function init(){
    ballArrry=[];
    for (var i=0;i<2;i++){
        //zufälliger x und y kordi
        var y =Math.random()*Math.round((window.innerHeight/100)*76)+20;
        var x = Math.random()*Math.round((window.innerWidth/100)*89)+40;
        //zufälige richtung
        var xm = (Math.random()*3)-2;
        var ym = (Math.random()*3)-2;
        var kreis = new Kreis(x, y, xm, ym, 30, '#4eb5f1')
        ballArrry.push(kreis)
    }
}


//event loop
function animate(){
    if (startstop){
        requestAnimationFrame(animate);
        //clear
        c.clearRect(0, 0, can_innerHeight, can_innerWidth)

        // um auf veränderung des fenster zu reagiren
        var can_innerHeight=Math.round((window.innerHeight/100)*83);
        canvas.height= can_innerHeight;
        var can_innerWidth=Math.round((window.innerWidth/100)*93);
        canvas.width=can_innerWidth;

        //aufrufen der update function für jedes objekt
        for (var i=0; i<ballArrry.length;i++)
        ballArrry[i].update(can_innerHeight,can_innerWidth);
        console.log(distans(ballArrry[0], ballArrry[1]));
    }
}