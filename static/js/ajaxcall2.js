$('#get_button').click(function(){
     $('#loadingmessage').show();
     $.ajax({

              url: "/chief_perdate",
              data : {from:$('#datepicker1').val(),to:$('#datepicker2').val()},
              type: 'POST',
              dataType: "JSON",
              success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }

             });
});

 $("#selectField2").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc_chief",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });


     $("#type2").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc_chief",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });