// Get modal element
const modal=document.getElementById("myModak");

// Get buttons
const openModalBtn= document.getElementById("openModalBtn");
const closeModalBtn= document.getElementById("closeModalBtn");
const alertBtn= document.getElementById("alertBtn");

// Open modal on button click 
openModalBtn.onclick=function(){
    modal.style.display="block";
}

// Open modal on button click 
openModalBtn.onclick=function(){
    modal.style.display="none";
}

// Open modal on button click 
window.onclick=function(event){
    if (event.target=== modal){
        modal.style.display="none";
    }
   
}
// show alert on button click
alertBtn.onclick=function(){
    alert(" this is a simple pop up alert HOW ABOUT THEM COWBOYS ")
}
