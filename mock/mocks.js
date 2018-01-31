var Swagmock = require('swagmock');
var routes = Swagmock('./routes.yml');

COLOR = "\x1b[34;1m"

routes.responses({
   path: '/catalog',
   operation: 'get',
   response: 200 
}, function(error, mock) {
    console.log(COLOR, "Le client récupére des chambres\x1b[0m\n/catalog get", JSON.stringify(mock, null, 4));
});

routes.responses({
    path: '/price',
    operation: 'get',
    response: 200,
    useExamples: true
}, function(error, mock) {
    console.log(COLOR, "Le client récupére le prix pour cette chambre\x1b[0m\n/price get", mock);
});

routes.responses({
   path: '/book',
   operation: 'get',
   response: 200 
}, function(error, mock) {
    console.log(COLOR, "Le client récupère les dates de réservation pour cette chambre\x1b[0m \n/book get", mock);
});

routes.responses({
   path: '/book',
   operation: 'post',
   response: 200 
}, function(error, mock) {
    console.log(COLOR, "Le client reserve la chambre\x1b[0m\n/book post", JSON.stringify(mock));
});

routes.responses({
   path: '/mail',
   operation: 'post',
   response: 200 
}, function(error, mock) {
    console.log(COLOR, "Un mail de confirmation est envoyé au client\x1b[0m\n/mail post", JSON.stringify(mock));
});

routes.responses({
    path: '/register_user',
    operation: 'post',
    response: 200
}, function(error, mock) {
    console.log(COLOR, "Un user enregistre un nouvel user\x1b[0m\n/register_user post", JSON.stringify(mock));
});

routes.responses({
    path: '/login_user',
    operation: 'post',
    response: 200
}, function(error, mock) {
    console.log(COLOR, "Un user se connecte\x1b[0m\n/login_user post", JSON.stringify(mock));
});

routes.responses({
    path: '/catalog/hotel',
    operation: 'post',
    response: 200
}, function(err, mock) {
    console.log(COLOR, "Un user admin ajoute ensuite un hotel\x1b[0m\n/catalog/hotel post", JSON.stringify(mock));
});

routes.responses({
   path: '/catalog/room',
   operation: 'post',
   response: 200 
}, function(err, mock) {
    console.log(COLOR, "Un user admin ajoute une chambre\x1b[0m\n/catalog/room post", JSON.stringify(mock));
});

routes.responses({
   path: '/price/room',
   operation: 'patch',
   response: 200 
}, function(err, mock) {
    console.log(COLOR, "Un admin augmente le prix d'une chambre\x1b[0m\n/price/room patch", JSON.stringify(mock));
});

routes.responses({
   path: '/price/increase',
   operation: 'patch',
   response: 200 
}, function(err, mock) {
    console.log(COLOR, "Un admin augemente le coeff\x1b[0m\n/price/increase patch", JSON.stringify(mock));
});
