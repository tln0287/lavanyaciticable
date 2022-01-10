$('#get_button').click(function(){
     $('#loadingmessage').show();
     $.ajax({
              url: "/restaurants_perdate",
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


 $("#selectField").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc",
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

     $("#selectedproduct").change(function () {
        from = this.value;

        $.ajax({
            type: "POST",
            url:"/productcal",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
            alert(response);
                 $('#loadingmessage').hide();
                 $('#newmrp').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });

     $("#selectedproduct1").change(function () {
        from = this.value;
        alert("hi");
        $.ajax({
            type: "POST",
            url:"/productcal",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
            alert(response);
                 $('#loadingmessage').hide();
                 $('#newmrp').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });

     $("#product2").change(function () {
        from = this.value;
        alert("hi");
        $.ajax({
            type: "POST",
            url:"/productcal2",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
            alert(response);
                 $('#loadingmessage').hide();
                 $('#newmrp').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });

     $("#type").change(function ()
     {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response)
            {
                 $('#loadingmessage').hide();
                 $('#latest').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error)
                    {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });