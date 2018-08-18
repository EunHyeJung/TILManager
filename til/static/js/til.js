function show_til_detail(pk) {
    $.ajax({
        type : 'GET',
        url : '/tils/' + pk,
        contentType : 'application/json; charset=utf-8',
        success : function(response) {
            var data = response;
            var html = '<a class="btn btn-default" href="{% url til_edit pk=item.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>';
            var post_data = JSON.parse(response.post);
            var post_pk = post_data[0].pk;
            html += '<a href="javascript:delete_post('+ post_pk + ');" class="btn btn-default"><span class="glyphicon glyphicon-trash"></span></a>'
            $('.contents-head').html(html);

            //console.log(data);
            var til_data = JSON.parse(response.tils);
            var html = '<h2> TIL </h2> <br/> <ul>';
            for(i = 0; i < til_data.length; i++) {
                til_item =  til_data[i].fields.item;
                html +=  '<li>' + til_item + '</li>';
            }
            html += '</ul>';
            $('#til').html(html);

            var review_data = JSON.parse(response.reviews);
            var html = '<h2> REVIEW </h2> <br/> <ul>';
            for(i = 0; i < review_data.length; i++) {
                review_item =  review_data[i].fields.item;
                html +=  '<li>' + review_item + '</li>';
            }
            html += '</ul>';
            $('#review').html(html);

            var plan_data = JSON.parse(response.plans);
            var html = '<h2> PLAN </h2> <br/> <ul>';
            for(i = 0; i < plan_data.length; i++) {
                plan_item =  plan_data[i].fields.item;
                html +=  '<li>' + plan_item + '</li>';
            }
            html += '</ul>';
            $('#plan').html(html);


        }
    })
}
/////////////////////////
function delete_post(pk) {
    var r = confirm("확인을 누르면 해당 TIL이 삭제됩니다.")
    if(r) {
//        $.ajax({
//            type : 'POST',
//            url : '/tils/' + pk + '/delete',
//            success : function(response) {
//
//            }
//        })
        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", '/tils/' + pk + '/delete', true);
        xhttp.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        xhttp.send();

    }
}


////////////////////
$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', 'form');
    return false;
});

function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    console.log(selector + " : " + prefix);

    newElement.find(':input').each(function() {
        console.log("input chekc");
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        console.log("name : " + name);
    });

    return false;
}