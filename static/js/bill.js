$(document).ready(function () {

    var table


    function addbill(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "bill",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache",
                "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
           $.notify("Bill Added Successfully", {"status":"success"});

           $('.modal.in').modal('hide')
           table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getbill()
        });

    }

    function deletebill(BILL_ID) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "bill/" + BILL_ID,
            "method": "DELETE",
            "headers": {
                "cache-control": "no-cache",
                "postman-token": "28ea8360-5af0-1d11-e595-485a109760f2"
            }
        }

        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this data",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            closeOnConfirm: false
        }, function() {
           $.ajax(settings).done(function (response) {
             swal("Deleted!", "bill has been deleted.", "success");
             table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getbill()
        });


       });

    }



    function getbill() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "bill",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {

            for(i=0;i<response.length;i++){
                response[i].totalCost=response[i].Operation_Cost+response[i].Test_Cost
                // response[i].doc_fullname=response[i].D_name
                // response[i].receptionist_name=response[i].Recept_name
            }



            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                "aaSorting": [],
                aoColumns: [
                {
                    mData: 'First_Name'
                },
                {
                    mData: 'Last_Name'
                },
                {
                    mData: 'Visited_Date'
                },
                {
                    mData: 'Insurance_ID'
                },
                {
                    mData: 'Operation_Name'
                },
                {
                    mData: 'Operation_Cost'
                },
                {
                    mData: 'Test_Name'
                },
                {
                    mData: 'Test_Cost'
                },
                {
                    mData: 'totalCost'
                },
                // {
                //     mRender: function (o) {
                //         return '<button class="btn-xs btn btn-danger delete-btn" type="button">Delete</button>';
                //     }
                // }
                ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deletebill(data.BILL_ID)

            });


        });


    }




    $("#addpatient").click(function () {
        $('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

            $("#doctor_select").html(doctorSelect)
            $("#patient_select").html(patientSelect)
            $("#recept_select").html(receptionistSelect)

            $(".form_datetime").datetimepicker({
               format: 'yyyy-mm-dd hh:ii:ss',
               startDate:new Date(),
               initialDate: new Date()
           });
            console.log("innn")
            $("#savethepatient").off("click").on("click", function(e) {
                console.log("inn")
                var instance = $('#detailform').parsley();
                instance.validate()
                if(instance.isValid()){
                    jsondata = $('#detailform').serializeJSON();
                    addbill(jsondata)
                }

            })

        })



    })


    var doctorSelect=""
    function getDoctor() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "doctor",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {

            for(i=0;i<response.length;i++){

                response[i].doc_fullname=response[i].D_name
                doctorSelect +="<option value="+response[i].D_id+">"+response[i].doc_fullname+"</option>"
            }


        })
    }
    var patientSelect=""
    function getPatient() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {
            console.log(response)
           for(i=0;i<response.length;i++){
              response[i].pat_fullname=response[i].P_name
              patientSelect +="<option value="+response[i].P_id+">"+response[i].pat_fullname+"</option>"
          }

      })
    }
    var receptionistSelect=""
    function getRecept() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "Receptionist",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {
            console.log(response)
            for(i=0;i<response.length;i++){

                response[i].receptionist_name=response[i].Recept_name
                receptionistSelect +="<option value="+response[i].Recept_id+">"+response[i].receptionist_name+"</option>"
            }


        })
    }

    // getDoctor()
    // getPatient()
    // getRecept()
    getbill()
})