angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    

.state('libreriaCooprudea', {
    url: '/page1',
    templateUrl: 'templates/libreriaCooprudea.html',
    controller: 'libreriaCooprudeaCtrl'
  })

  .state('login', {
    url: '/page2',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('registrese', {
    url: '/page3',
    templateUrl: 'templates/registrese.html',
    controller: 'registreseCtrl'
  })

  .state('acuerdoDeLicencia', {
    url: '/page4',
    templateUrl: 'templates/acuerdoDeLicencia.html',
    controller: 'acuerdoDeLicenciaCtrl'
  })

  .state('categorias', {
    url: '/page5',
    templateUrl: 'templates/categorias.html',
    controller: 'categoriasCtrl'
  })

  .state('articulo', {
    url: '/page7',
    templateUrl: 'templates/articulo.html',
    controller: 'articuloCtrl'
  })

  .state('carroDeCompras', {
    url: '/page8',
    templateUrl: 'templates/carroDeCompras.html',
    controller: 'carroDeComprasCtrl'
  })

  .state('listaDeDeseos', {
    url: '/page9',
    templateUrl: 'templates/listaDeDeseos.html',
    controller: 'listaDeDeseosCtrl'
  })

$urlRouterProvider.otherwise('/page1')


});