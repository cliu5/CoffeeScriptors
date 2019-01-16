var lis=document.getElementsByName('type');
console.log();

for(var i=0; i<lis.length,i++){
    lis.addEventListener('mouseover',function(e){
	lis[i].style.opacity = "1";
    })
    if(lis[i].clicked == true){			
	lis[i].addEventListener('click',function(e){
	    element.style.opacity = "0.5";
	})
    }
    lis[i].addEventListener('click',function(e){
	lis[i].style.opacity = "1";
    })

}
