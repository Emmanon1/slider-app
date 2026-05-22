import base64, os

IMG1 = 'WhatsApp Image 2026-05-19 at 13.30.24 (1).jpeg'
IMG2 = 'WhatsApp Image 2026-05-19 at 13.30.24.jpeg'
OUTPUT = 'slider_v3.html'

def img_to_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')

b64_1 = img_to_b64(IMG1)
b64_2 = img_to_b64(IMG2)

html = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Slider</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;touch-action:none;-webkit-touch-callout:none;-webkit-user-select:none;user-select:none}
.sc{position:relative;width:100%;height:100%;overflow:hidden}
.sw{display:flex;width:200%;height:100%;transition:transform 0.4s ease}
.sl{width:50%;height:100%;flex-shrink:0}
.sl img{width:100%;height:100%;object-fit:contain;pointer-events:none;-webkit-user-drag:none}
.ctrl{position:absolute;bottom:0;left:0;width:100%;height:25%;opacity:0;z-index:100;cursor:grab}
</style>
</head>
<body>
<div class="sc">
<div class="sw" id="sw">
<div class="sl"><img src="data:image/jpeg;base64,''' + b64_1 + '''" alt="Photo 1"></div>
<div class="sl"><img src="data:image/jpeg;base64,''' + b64_2 + '''" alt="Photo 2"></div>
</div>
<div class="ctrl" id="ctrl"></div>
</div>
<script>
(function(){
var ctrl=document.getElementById('ctrl');
var sw=document.getElementById('sw');
var startX=0,currentX=0,dragging=false,done=false;

function onStart(e){
    if(done)return;
    dragging=true;
    startX=e.touches?e.touches[0].clientX:e.clientX;
    currentX=startX;
    sw.style.transition="none";
}

function onMove(e){
    if(!dragging||done)return;
    e.preventDefault();
    currentX=e.touches?e.touches[0].clientX:e.clientX;
    var diff=startX-currentX;
    if(diff>0){
        var pct=Math.min(diff/window.innerWidth*100,50);
        sw.style.transform="translateX(-"+pct+"%)";
    }
}

function onEnd(e){
    if(!dragging||done)return;
    dragging=false;
    var diff=startX-currentX;
    if(diff>80){
        done=true;
        sw.style.transition="transform 0.4s ease";
        sw.style.transform="translateX(-50%)";
        setTimeout(function(){window.location.href="commande_confirmee.html";},1500);
    }else{
        sw.style.transition="transform 0.3s ease";
        sw.style.transform="translateX(0)";
    }
}

ctrl.addEventListener("mousedown",onStart);
ctrl.addEventListener("touchstart",onStart,{passive:true});
document.addEventListener("mousemove",onMove);
document.addEventListener("touchmove",onMove,{passive:false});
document.addEventListener("mouseup",onEnd);
document.addEventListener("touchend",onEnd);
})();
</script>
</body>
</html>'''

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'OK: {OUTPUT} generated ({len(html)} bytes)')
