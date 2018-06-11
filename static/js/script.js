function openNav() {
    document.getElementById("mySidenav").style.width = "20%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
$(document).ready(function(){
    // $('.image-details').mouseenter(function(){
    //     $('.image-details').addClass('darken')
    // })
    // $('.image-details').mouseleave(function(){
    //     $('.image-details').removeClass('darken')
    // })

    $('.tool-tip').click(function(){
        copyURL = document.getElementById('img-copy')
        copyURL.select();
        document.execCommand('copy');

        toolTip = document.getElementById('tip');
        toolTip.innerHTML = 'Copied!'
    })
    $('.tool-tip').mouseleave(function(){
        toolTip = document.getElementById('tip')
        toolTip.innerHTML = 'Copy Link'
    })
})