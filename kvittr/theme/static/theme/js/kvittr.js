$(document).ready(function(){
    //How the like-button works
    //Updates likes for a special message id (pip_id)
    //Updates on both sites (listing and details)
    $(".pip_add_likes").click(function(event) {
        event.preventDefault();
        var pip_id = $(this).data("pip_id");
        $.ajax({
            url: '/pips_messages/pip_add_likes/' + pip_id
        })
        .done(function(data){
            var likes_updated = data['likes_updated'];
            var pip_add_likes = "#id-points-for-pip-" + pip_id;
            $(pip_add_likes).html(likes_updated + ' '  + "Likes");       
        });
    });
});