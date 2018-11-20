


$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post()
});

function create_post() {

   // console.log("#name").val() // sanity check
   var my_date = $('#materialUnchecked').is(":checked");
   var my_date1 = $('#materialUnchecked1').is(":checked");

    $.ajax({
        url : "/",
        type : "POST", // http method
        data : {     fullname : $('#fullname').val(),
        
                     email : $('#email').val(),
                     date1 : my_date1,
                     date2 : my_date,
                     csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                     },

        success : function(json) {
            $('#fullname').val('');
            $('#email').val('');
            $('#materialUnchecked').attr('checked', false);
            console.log("success", $('#materialUnchecked'), $('#materialUnchecked1')); // another sanity check
            toastr["success"]("Your request has been successful. See you there!")
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            toastr["error"]("Sorry, please try that again - make sure you select a date!")
        }
    });
};
