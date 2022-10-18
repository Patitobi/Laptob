function start(){
    World.update();
    Player1.update();
}
function main(){
    World.draw();
}
function end(){

}
function skip2(){

}
function skip5(){

}

class PlayMap{
    constructor(lowMax, topMax, rMax, lMax, player){
        this.lowMax = lowMax;
        this.topMax = topMax;
        this.rMax =rMax;
        this.lMax = lMax;
        this.objInWorld=[[],[],[]];
        this.playerX=undefined;
        this.playerY=undefined;
        this.Player=player;

        this.prep();
    }
    update(){
        for(var i=0; i<this.objInWorld.length;i++){
            for(var e=0; e<this.length;e++){
                this.objInWorld[i][e].update();
            }
        }
    }
    
    draw(){
        for(var i=0; i<this.objInWorld.length;i++){
            for(var e=0; e<this.objInWorld[i].length;e++){
                this.objInWorld[i][e].draw();
            }
        }
    }
    prep(){
        this.player=Player1;
        this.playerX=Player1.x;
        this.playery=Player1.y;

        this.atBlock(0, newCanInnerHeight-50, newCanInnerWidth, 50 , '#4eb5f1');
    }
    atBlock( x, y, a, b, collor){
        this.objInWorld[1].push(new MapBlock(a, b, x, y, collor));
    }
    atCir(range, x , y, collor){
        this.objInWorld[2].push(new MapCir(range, x, y, collor));
    }
}
class MapBlock{
    constructor(a, b, x, y, collor){
        this.x=x;
        this.y=y;
        this.width=a;
        this.height=b;
        this.collor=collor;
    }
    draw(){
        c.fillStyle=this.collor;
        c.fillRect(this.x, this.y, this.width, this.height);
    }
    update(){
        
    }
}
class MapCir{
    constructor(range, x, y, collor){
        this.x=x;
        this.y=y;
        this.range=range;
        this.collor=collor;
    }
    draw(){
        c.beginPath();
        c.arc(this.x, this.y, this.radius, 0, Math.PI*2, false);
        c.strokeStyle=this.collor;
        c.stroke();
    }
    update(){

    }
}
class Player {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.dy = 0;
        this.dx = 1;
        this.collor = '#4eb5f1';
    }
    update() {

        this.x+=this.dx;
        this.y+=this.dy;
        this.draw();
    }
    draw(){
        c.translate(this.x, this.y);
        c.fillStyle=this.collor;
        c.beginPath();
        c.arc(0, 0, 20, 0, Math.PI*2, false);
        c.fill();
        c.strokeStyle=this.collor;
        c.stroke();
        c.fillRect(-10, 25, 20, 60);
    }
}

//event loop
function frame(){
    if (startstop){
        requestAnimationFrame(frame);
        // um auf veränderung des fenster zu reagiren
        newCanInnerHeight=Math.round((window.innerHeight/100)*83);
        newCanInnerWidth=Math.round((window.innerWidth/100)*93);

        canvas.width=newCanInnerWidth;
        canvas.height=newCanInnerHeight;
        //clear
        c.clearRect(0, 0, newCanInnerHeight, newCanInnerWidth)

        start();

        main();

        index2+=1;
        index5+=1;

        if (index2==2){
            index2=0;
            skip2();
        }
        if (index5==5){
            index5=0;
            skip5();
        }

        end();
        
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
    frame();
}

//zufäliger integer zwichen 2 werten
function random(min, max){
    return Math.floor(Math.random()*(max-min+1)+min);
}

// festlegen von größe und sonnstige pflicht sachen
var canvas = document.querySelector('canvas');
var startstop = false;
var c = canvas.getContext('2d');

var newCanInnerHeight=Math.round((window.innerHeight/100)*83);
var newCanInnerWidth=Math.round((window.innerWidth/100)*93);
var oldCanInnerWidth= undefined;
var oldCanInnerHeight= undefined;
canvas.height= newCanInnerHeight;
canvas.width=newCanInnerWidth;

var index2 = 0;
var index5 = 0;

var Player1=new Player(500, 500);
var World=new PlayMap(0, newCanInnerHeight, newCanInnerWidth, 0, Player1);