
function getData() 
{

  //alert ( "estoy entrando a get Data");

	sessionStorage.filial = "puebla";

    jQuery.support.cors = true;
    try
    {                         
     $.ajax({
        url: "/gettweets",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: true,
        data: {filial: sessionStorage.filial},                         
        type: 'get',
        crossDomain: true,
        success: function(response) {
	  tweets = response;
          //alert(response);
          tweets.forEach(function (tweet) 
          {
             var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
  			" data-wow-delay='0.2s'> " +
                        "<img src='" + tweet.urlImage + "'" +
                        " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
                        " >" +
                        " <div class='section-title wow bounceIn'> " +
                        "<h3>" + tweet.title + "</h3>" +
                        "<h5>" + tweet.description + "</h5>" +
                        "</div>" +
                        "</div>" 
                       $("#tweets").append(nombre);
          });
	       getMedicinas()
 	      }
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}

function getMedicinas() 
{

  //alert ( "estoy entrando a get Data");

  sessionStorage.filial = "puebla";

    jQuery.support.cors = true;
    try
    {                         
     $.ajax({
        url: "/getmedicinas",
        dataType: 'json',
        cache: false,
        contentType: false,
        processData: true,
        data: {filial: sessionStorage.filial},                         
        type: 'get',
        crossDomain: true,
        success: function(response) {
    medicinas = response;
          alert(response);
          medicinas.forEach(function (medicina) 
          {
             var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
        " data-wow-delay='0.2s'> " +
                        "<img src='" + medicina.urlImage + "'" +
                        " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
                        " >" +
                        " <div class='section-title wow bounceIn'> " +
                        "<h3>" + medicina.title + "</h3>" +
                        "<h5>" + medicina.description + "</h5>" +
                        "</div>" +
                        "</div>" 
                       $("#medicinas").append(nombre);
          });
        }
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}
