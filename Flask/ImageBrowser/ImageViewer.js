
var socket = io.connect();

$(document).ready(function(){
  // Receive
  socket.on('PutImageResponse', function(msg){
    // 리스트 추가
    if (msg.length > 0)
    {
        ImageViewer(msg);
    }
  });
});


function getImageList(dir_name){
    socket.emit("GetImageRequest", {data:dir_name});
}

columnmax = 5;
function ImageViewer(item) {

    img_viewer = document.getElementById('IMAGE_BOARD');
    img_viewer.innerHTML = "";
    
    // 이미지 링크 Tag 템플릿을 정의함, 이후에 {0}, {1}을 경로로 변경 사용함.
    base_tag = ""
    i_tag = "<a href='{0}' data-fancybox='images'><img src='{1}' style='border: 1px' /></a>"


    for (i=0; i < item.length; i++)
    {  
        image_path = item[i].dirname + "/" + item[i].filename;
        t_tag = i_tag.replace("{0}", image_path); 
        t_tag = t_tag.replace("{1}", image_path); 

        base_tag += t_tag;
    }
    
    img_viewer.innerHTML += base_tag;

}
