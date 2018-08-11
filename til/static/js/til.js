function show_til_detail(pk) {
    $.ajax({
        type : 'GET',
        url : '/tils/' + pk,
        contentType : 'application/json; charset=utf-8',
        success : function(response) {
            var data = response;

            //console.log(data);
            var til_data = JSON.parse(response.tils);
            var html = '<h2> TIL </h2> <br/> <ul>';
            for(i = 0; i < til_data.length; i++) {
                til_item =  til_data[i].fields.til_item;
                html +=  '<li>' + til_item + '</li>';
            }
            html += '</ul>';
            $('#til').html(html);

            var review_data = JSON.parse(response.reviews);
            var html = '<h2> REVIEW </h2> <br/> <ul>';
            for(i = 0; i < review_data.length; i++) {
                review_item =  review_data[i].fields.review_item;
                html +=  '<li>' + review_item + '</li>';
            }
            html += '</ul>';
            $('#review').html(html);

            var plan_data = JSON.parse(response.plans);
            var html = '<h2> PLAN </h2> <br/> <ul>';
            for(i = 0; i < plan_data.length; i++) {
                plan_item =  plan_data[i].fields.plan_item;
                html +=  '<li>' + plan_item + '</li>';
            }
            html += '</ul>';
            $('#plan').html(html);


        }
    })
}

$( document ).ready(function() {

});

