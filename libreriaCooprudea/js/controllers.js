angular.module('app.controllers', [])
  
.controller('libreriaCooprudeaCtrl', ['$scope', '$stateParams', '$http', '$location', 'CategoriasExistentes', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams, $http, $location, CategoriasExistentes) {

        $scope.$on("$ionicSlides.sliderInitialized", function () {
                
            var req = {
                method: 'GET',
                url: 'http://lopera.co/obtenerTodasCategorias'
            };
            $http(req).then(function successCallback(response) {
                $scope.banners = response['data'];
                CategoriasExistentes.data=$scope.banners;
              }, function errorCallback(response) {
                $scope.banners = {};
            })
        });
   
}])

    
.controller('loginCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('registreseCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('acuerdoDeLicenciaCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('categoriasCtrl', ['$scope', '$stateParams', '$http', '$location', 'CategoriasExistentes', 'TiposDeBusqueda',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
                           
                           
function ($scope, $stateParams, $http, $location, CategoriasExistentes, TiposDeBusqueda) {
    
        $scope.$on('$ionicView.afterEnter', function () {
        
            $scope.rcategorias=CategoriasExistentes.data;
            $scope.tbusqueda=TiposDeBusqueda.data;
            $scope.buscarXcategoria('1');
            
        });
       
    
        $scope.buscarXcategoria = function (categoria='') {
            console.log(categoria);
            var req = {
                method: 'GET',
                url: 'http://192.168.2.248:80/obtenerProductosCategoria?categoria='+categoria
            };
            $http(req).then(function successCallback(response) {
                $scope.libros = response['data'];
              }, function errorCallback(response) {
                console.log("Error al consultar");
                $scope.respuesta = {};
            })
        };
    
        $scope.cambiarTipoBusqueda = function (tipo='') {
            console.log(tipo);
            EstadoTiposBusqueda.data=tipo;
        };
    
    

    $scope.buscarXisbn = function (isbn='') {
            console.log(isbn);
            var req = {
                method: 'GET',
                url: 'http://192.168.2.248:80/obtenerProductosCategoria?categoria='+isbn
            };
            $http(req).then(function successCallback(response) {
                $scope.libros = response['data'];
                
              }, function errorCallback(response) {
                console.log("Error al consultar");
                $scope.respuesta = {};
            })
        };
    
   
}])
   
.controller('articuloCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('carroDeComprasCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('listaDeDeseosCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
 