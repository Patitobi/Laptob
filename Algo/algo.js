// festlegen von größe und sonnstige pflicht sachen
var canvas = document.querySelector('canvas');
var startstop = false;
var c = canvas.getContext('2d');

canvas.height= Math.round((window.innerHeight/100)*83);
canvas.width=Math.round((window.innerWidth/100)*93);

//kreis objekt
function Kreis(x, y, xm, ym, radius, collor){
    this.x=x;
    this.y=y;
    this.xm=xm;
    this.ym=ym;
    this.radius=radius;
    this.collor=collor;

    //bildet objekt in canvas ab
    this.draw = function(){
        c.beginPath();
        c.arc(this.x, this.y, this.radius, 0, Math.PI*2, false);
        c.strokeStyle=this.collor;
        c.stroke();
    }
    //checkt für bedingungen jeden durlauf
    this.update = function(can_innerHeight, can_innerWidth){

        //wenn am rand (lings rechts)
        if(this.x+this.radius > can_innerWidth || this.x-this.radius < 0){
            this.xm=this.xm*-1;
        }
        //wenn am rand (oben unten)
        if(this.y+this.radius > can_innerHeight || this.y-this.radius < 0){
            this.ym=this.ym*-1;
        }

        //neue position
        this.x=this.x+this.xm;
        this.y=this.y+this.ym;

        this.draw();
    }
}

//start und stop knopf
function start_stop(x){
    if(x && !startstop){
        startstop=true;
    }
    else if(!x && startstop){
        startstop = false;
    }
        animate();
}

// erstellen von objekten
var kreisarry=[];

for (var i=0; i<1000; i++){
    //zufäliger spann ohne das in der wand gespant wird
    var y =Math.random()*Math.round((window.innerHeight/100)*76)+30;
    var x = Math.random()*Math.round((window.innerWidth/100)*86)+30;
    // zufälige erste richtung
    var xm = (Math.random()*3)-2;
    var ym = (Math.random()*3)-2;
    var kreis = new Kreis(x, y, xm, ym, 30, '#4eb5f1')
    kreisarry.push(kreis);
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
        for (var i=0; i < kreisarry.length; i++){
            kreisarry[i].update(can_innerHeight, can_innerWidth);
        }
    }
}