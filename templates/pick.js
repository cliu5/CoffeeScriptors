var list = document.getElementsByTagName('img');
console.log(list);

for(var i = 0; i < list.length; i++){
    var node = list[i];
    console.log(node);
    node.addEventListener('mouseover',function(e){
	node.style.opacity = "1";
    });
    node.addEventListener('mouseout',function(e){
	node.style.opacity = "0.5";
    });
    node.addEventListener('clicked',function(e){
	node.style.opacity = "1";
    });
}
