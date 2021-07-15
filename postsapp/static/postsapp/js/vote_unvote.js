function vote_unvote(postid) {
    var icon_id = '#icon-' + postid;
    var votes_id = '#votes-' + postid;
    $.ajax({
        type: 'POST', url: '/vote_post/',
        data: {'csrfmiddlewaretoken': csrf_token, 'postid': postid},
        dataType: 'json',
        cache: false,
        success: function (response) {
            if (response.success) {
                $(votes_id).text(parseInt($(votes_id).text()) + 1);
                $(icon_id).attr('class', 'fas fa-caret-square-down');
            } else {
                $(votes_id).text(parseInt($(votes_id).text()) - 1);
                $(icon_id).attr('class', 'fas fa-caret-square-up');
            }
        }
    });
}