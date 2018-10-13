angular.module('AppChat').controller('SignUpController', function($scope, $routeParams, $location, $http, $log){


    this.signup = function(){
        console.log('Partially working.');
        var data = {};
        data.first_name = this.first_name;
        data.last_name = this.last_name;
        data.e_mail = this.e_mail;
        data.phone = this.phone;
        data.password = this.password;
        data.user_name = this.user_name;


        var reqURL = "http://localhost:5000/SignUp";

        var config = {
            headers: {
                'Content-Type': 'application/json;charset=utf-8;'
            }
        }

        $http.post(reqURL, data, config).then(
            function(response){
                alert("Successful signup.")

                $location.url('/login')
            },
            function(response){
                var status = response.status;

                console.log(data);


                if(status == 0){
                    alert("No internet connection.");
                }else if(status == 401){
                    alert("Your session has expired.")
                }else if(status == 403){
                    alert("You are not authorized to use the system.")
                }else if(status == 404){
                    console.log('fuck!!!!');
                    alert("Requested information not found")
                }else{
                    alert("Internal System Error")
                }
            }
        )
    }
})