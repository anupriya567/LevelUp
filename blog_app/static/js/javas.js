
// console.log("script is ok")

// let itemimg = document.getElementsByClassName('itemimg');
// console.log(itemimg);
// console.log("hello");
// // Array.from(itemimg).forEach(element => {
    
// //     element.addEventListener('mouseover',function(e)
// //     {
// //         console.log("on mouseover");
// //         e.style.width = "280px";

// //     })
 
// // });

// Array.from(itemimg).forEach(element => {
    
//     element.addEventListener('mouseOut',function(e)
//     {
//         console.log("on blurr");
//         e.style.width = "100px";

//     })
// });


const pa = document.getElementsByClassName("aboutside")[0]

var child = pa.getElementsByClassName("aboutin")[0]
var removed = pa.removeChild(child)
pa.appendChild(removed)