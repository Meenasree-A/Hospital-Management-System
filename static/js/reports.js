$(document).ready(function () {

    var table

    function addReports(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "reports",
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
            $('.modal.in').modal('hide')
            $.notify("Report details added Successfully", { "status": "success" });
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getReports()
        });

    }

    function deleteReports(Report_ID) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "reports/" + Report_ID,
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
        }, function () {
            $.ajax(settings).done(function (response) {
                swal("Deleted!", "Report details has been deleted.", "success");
                table.destroy();
                $('#datatable4 tbody').empty(); // empty in case the columns change
                getReports()
            });


        });

    }

    function updateReports(data, Report_ID) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "reports/" + Report_ID,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Report details Updated Successfully", { "status": "success" });
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getReports()
        });


    }

    function getReports() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "reports",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {



            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                "aaSorting": [],
                aoColumns: [
                    {
                        mData: 'Report_ID'
                    },
                    {
                        mData: 'Name'
                    },
                    {
                        mData: 'Description'
                    },
                    {
                        mData: 'Medical_Tests_Test_ID'
                    },
                    {
                        mData: 'Patient_Patient_ID'
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-info btn-edit" type="button">Edit</button>';
                        }
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-danger delete-btn" type="button">Delete</button>';
                        }
                    }
                ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deleteReports(data.Report_ID)

            });
            $('.btn-edit').one("click", function (e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savethereport").off("click").on("click", function (e) {
                        var instance = $('#detailform').parsley();
                        instance.validate()
                        console.log(instance.isValid())
                        if (instance.isValid()) {
                            jsondata = $('#detailform').serializeJSON();
                            updateReports(jsondata, data.Report_ID)
                        }

                    })
                })



            });

        });


    }




    $("#addReports").click(function () {
        $('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

            console.log('innn')
            $("#savethereport").off("click").on("click", function (e) {
                console.log("inn")
                var instance = $('#detailform').parsley();
                instance.validate()
                if (instance.isValid()) {
                    jsondata = $('#detailform').serializeJSON();
                    addReports(jsondata)
                }

            })

        })



    })


    getReports()
})
