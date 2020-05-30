
$(document).ready(function(){
   
    $("#createButton").click(function() {
        var serializedData=
        $("#createTaskForm").serialize();
        /* console.log(serializedData) */

        $.ajax({
            url:$('createTaskForm').data('url'),
            data:serializedData,
            type:'post',
            success:function(response) {
                $('#tasklist')
            }

        })
    });
});