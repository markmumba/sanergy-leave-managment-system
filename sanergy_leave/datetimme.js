{/* <link rel= "StyleSheet" href = "jquery.datetimepicker.min.css">
<script src="jquery.js"></script>
<script src="https://apis.google.com/js/api:client.js"></script>

<input id="Begin_Date">
<input id="End_Date">

<button onclick="calulateDiff()">Calculate</button>
 */}

$("Begin_Date").datetimepicker({
    timepicker:false,
    format: 'Y-m-d'
});

$("End_Date").datetimepicker({
    timepicker:false,
    format: 'Y-m-d'
});

function calulateDiff(){
    // catch both dates 
    var Begin_Date = new Date($("#Begin_Date").val());
    var End_Date = new Date($("#End_Date").val());

    var timeDiff = End_Date.getTime() - Begin_Date.getTime();

    var milliSecondInaSecond = 1000;
    var secondsInanHour = 3600;
    var hoursInaDay = 24;
    daysDiff=0;

    var daysDiff = timeDiff / (milliSecondInaSecond * secondsInanHour * hoursInaDay );
}
