angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter = 0;
        this.newText = "";

        this.loadMessages = function(){

            var url ="http://localhost:5000/MessagesApp/messages";

            $http.get(url).then(function(response) {
                thisCtrl.messageList = response.data.Messages;
            },
            function (response){
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });


            // // Get the messages from the server through the rest api
            // thisCtrl.messageList.push({"id": 1, "text": "Hola Mi Amigo", "author" : "Bob",
            // "like" : 4, "nolike" : 1});
            // thisCtrl.messageList.push({"id": 2, "text": "Hello World", "author": "Joe",
            //     "like" : 11, "nolike" : 12});

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
            // console.log(thisCtrl.messageList);

        //     result['message_id'] = row[0]
        // result['user_name'] = row[1]
        // result['content'] = row[2]
        // result['reply_id'] = row[3]
        // result['time_stamp'] = row[4]
        // result['likes'] = row[5]
        // result['dislikes'] = row[6]
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"message_id": nextId, "content" : msg, "user_name" : author, "likes" : 0, "dislikes" : 0, "reply_id": null, "time_stamp":""});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);
