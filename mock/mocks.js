var Swagmock = require('swagmock');
var routes = Swagmock('./routes.yml');

routes.responses({
   path: '/catalog',
   operation: 'get',
   response: 200 
}, function(error, mock) {
    console.log("/cataog get", JSON.stringify(mock));
});

routes.responses({
    path: '/price',
    operation: 'get',
    response: 200
}, function(error, mock) {
    console.log("/price get", mock);
});

routes.responses({
   path: '/book',
   operation: 'get',
   response: 200 
}, function(error, mock) {
    console.log("/book get", mock);
});

routes.responses({
   path: '/book',
   operation: 'post',
   response: 200 
}, function(error, mock) {
    console.log("/book post", JSON.stringify(mock));
});

routes.responses({
   path: '/mail',
   operation: 'post',
   response: 200 
}, function(error, mock) {
    console.log("/mail post", JSON.stringify(mock));
});

routes.responses({
    path: '/register_user',
    operation: 'post',
    response: 200
}, function(error, mock) {
    console.log("/register_user post", JSON.stringify(mock));
});

routes.responses({
    path: '/login_user',
    operation: 'post',
    response: 200
}, function(error, mock) {
    console.log("/login_user post", JSON.stringify(mock));
});

routes.responses({
    path: '/catalog/hotel',
    operation: 'post',
    response: 200
}, function(err, mock) {
    console.log("/catalog/hotel post", JSON.stringify(mock));
});

routes.responses({
   path: '/catalog/room',
   operation: 'post',
   response: 200 
}, function(err, mock) {
    console.log("/catalog/room post", JSON.stringify(mock));
});

routes.responses({
   path: '/price/room',
   operation: 'patch',
   response: 200 
}, function(err, mock) {
    console.log("/price/room patch", JSON.stringify(mock));
});

routes.responses({
   path: '/price/increase',
   operation: 'patch',
   response: 200 
}, function(err, mock) {
    console.log("/price/increase patch", JSON.stringify(mock));
});
