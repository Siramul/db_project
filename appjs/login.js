angular.module('AppChat').controller('loginCtrl',['$scope', '$location', '$http', '$routeParams', "$http",
function($scope, $location, $http, $routeParams){

    thisCtrl = this;

    $scope.login = function(){
        console.log('Inside function');
        var user_name = $scope.user_name;
        var password = $scope.password;
        var url = "http://localhost:5000/Login";
        $http.post(url,user_name,password).then(
            function(response){
                console.log('Success');
                if(!angular.isUndefined(response.data.User)){
                    console.log(JSON.stringify(response.data));
                    $location.path('/chat');
                }else{
                    console.log('Fail');
                    console.log(response.data.ERROR);
                    alert(response.data.ERROR);
                }

                $scope.user_name = '';
                $scope.password = '';
                },
            function(response){
                var status = response.status;
                if(status){
                    console.log(status)
                }
            }
        )

    }

    $scope.signup = function(){
        $location.path('/chat')
    }

}]
