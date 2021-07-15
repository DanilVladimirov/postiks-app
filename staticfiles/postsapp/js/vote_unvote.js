function vote_unvote(pubid) {
    var icon_id = '#icon-' + pubid;
    var votes_id = '#votes-' + pubid;
    $.ajax({
        type: 'POST', url: '/vote_post/',
        data: {'csrfmiddlewaretoken': csrf_token, 'pubid': pubid},
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