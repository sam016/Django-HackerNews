(function() {

    var eleAbs = document.querySelectorAll(".absolute");

    window.onscroll = function(e) {
        if (window.scrollY >= 100) {
          for(var ele of eleAbs){
            if(ele.classList.contains("absolute")){
              ele.classList.remove("absolute");
              ele.classList.add("fixed_top");
            }
          }
        } else {
          for(var ele of eleAbs){
            if(ele.classList.contains("fixed_top")){
              ele.classList.remove("fixed_top");
              ele.classList.add("absolute");
            }
          }
        }
    }

})();
