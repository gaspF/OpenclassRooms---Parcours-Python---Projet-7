
var address = $('#address');
var maps = $('#map');
var addresseDonnee = $('#addresseDonnee');
var histoireWiki = $('#histoirewiki');
var wikiHistory = $('#wikiHistory');
var loader = $('#loader');
var button = $('#submit');
var goMap;

function initMap(lat, lng) {
        var location = {lat : lat, lng: lng};
        var goMap = new google.maps.Map(document.getElementById('map'), {scrollwheel: true, zoom: 8, center: location});
        var marker = new google.maps.Marker({position: location, map: goMap})
        }
 button.on('click', function(event) {
    event.preventDefault();
    address.hide();
    addresseDonnee.text('');
    histoireWiki.text('');
    maps.hide();
    $("#loading").show();

    $.ajax({
        url: '/_response',
        data: $('form').serialize(),
        dataType : 'json',
        type: 'GET',
        success : function(response){
            $("#loading").hide();
            maps.show();
            initMap(parseFloat(response['lat']), parseFloat(response['lng']))
            address.show();
             $("#chat ul").append('<li class="answer"><div class="speech-bubble">' + response['open_quote'] + '<br>' + response['address'] + '</div></li>');
             $("#chat ul").append('<li class="answer"><div class="speech-bubble">' + response['message_wiki'] + '<br>' + response['end_quote'] +'</div></li>');
            wikiHistory.show();


    }
    })

    });

