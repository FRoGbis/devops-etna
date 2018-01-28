var Swagmock = require('swagmock');
var routes = Swagmock('./routes.yml');

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
    console.log("/book post", mock);
});

routes.responses({
   path: '/catalog',
   operation: 'get',
   response: 200 
}, function(error, mock) {
    console.log("/cataog get", mock);
});
