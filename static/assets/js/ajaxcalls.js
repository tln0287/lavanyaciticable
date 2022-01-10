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


 $("#selectField5").change(function () {
        from = this.value;
              $.ajax({
            type: "POST",
            url:"/datefilters",
            data : {from:this.value},


            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#date_new').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();


                    }
        });
    });




 $("#selectField1").change(function () {
        from = this.value;
              $.ajax({
            type: "POST",
            url:"/subsc2",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest1').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });



     $("#productrow").change(function () {
        from = this.value;
              $.ajax({
            type: "POST",
            url:"/prow",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#pdata').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });


     $("#latest").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc1",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest2').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });

     $("#latest1").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/subsc3",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#latest3').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });



     $("#fromt").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/total_time1",
            data : {from:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#newone').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });

     $("#toti").change(function () {
        from = this.value;
        $.ajax({
            type: "POST",
            url:"/total_time",
            data : {to:this.value},
            dataType: "JSON",
            success : function(response){
                 $('#loadingmessage').hide();
                 $('#newone').html(response.data);

                 later_user.validateNow(true, false);

                    },
                    error: function (request, status, error) {
                        $('#loadingmessage').hide();
                        alert(request.response.data);

                    }
        });
    });