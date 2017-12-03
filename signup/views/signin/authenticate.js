$(document).ready(function() {
  $('#loginform').submit(function(e) {
    e.preventDefault();
    $.ajax({
    type: 'POST',
    url: 'http://dock2.hyunwookshin.com:8084/authenticate',
    data:{
            username: $("#username").val(),
            password: $("#password").val()
        },
    success: function(resultdata){
      $.ajax({
          type: 'GET',
          url: 'http://dock2.hyunwookshin.com:8044',
          headers: {"x-access-token": resultdata.token},
          success: function(newData){
              console.log('success');
              //console.log(newData);
              window.location= 'home.html'
         }
       });
  },
  complete: function () {
        // Schedule the next request when the current one has been completed

        setTimeout(this.ajaxRequest, 4000);
    }
 /*  });
  } */    
  });
 });
 $('#signup').submit(function(e) {
    e.preventDefault();
    $.ajax({
    type: 'POST',
    url: 'http://dock2.hyunwookshin.com:8084/signup',
    data:{
		    firstname:$("fname").val(),
			lastnmae :$("lname").val(),
            username: $("#username").val(),
            password: $("#password").val()
        },
    success: function(resultdata){
      $.ajax({
          type: 'GET',
          url: 'http://dock2.hyunwookshin.com:8084',
          headers: {"x-access-token": resultdata.token},
          success: function(newData){
              console.log('success');
              //console.log(newData);
              window.location= 'index.html'
         }
       });
  },
  complete: function () {
        // Schedule the next request when the current one has been completed

        setTimeout(this.ajaxRequest, 4000);
    }
 /*  });
  } */    
  });
 });
});

